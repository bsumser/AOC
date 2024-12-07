#include <bits/stdc++.h>
#include <string>
#include <thread>

using namespace std;

std::set<std::array<int, 2>> silver(vector<vector<char> > data, int &initRow, int &initCol);
int gold(vector<vector<char> > data, std::set<std::array<int, 2>> pos, int startRow, int startCol);
int gold_multi(vector<vector<char> > data, std::set<std::array<int, 2>> pos, int startRow, int startCol);
void processArray(vector<vector<char>>& data, vector<array<int, 2>>& arr, int start, int end, int startRow, int startCol, std::atomic<int>& globalSum);
int processElement(vector<vector<char> > data, int startRow, int startCol, int obsRow, int obsCol);
vector<vector<char> > parse_data(char* filename);
bool cycle_detect(vector<vector<char> > data, int startRow, int startCol);

int main(int argc, char* argv[]) {
    int initRow = 0, initCol = 0;
    vector<vector<char> > data = parse_data(argv[1]);
    std::set<std::array<int, 2>> pos = silver(data, initRow, initCol);
    //gold_multi(data, pos, initRow, initCol);
    gold(data, pos, initRow, initCol);

    return 0;
}

std::set<std::array<int, 2>> silver(vector<vector<char> > data, int &initRow, int &initCol) {
    int ans = 0;
    int startRow = 0;
    int startCol = 0;

    std::set<std::array<int, 2>> pos;
    
    for (int row = 0; row < data.size(); row++) {
        for (int col = 0; col < data[0].size(); col++) {
            if (data[row][col] == '^') {
                startRow = row, startCol = col;
                initRow = row, initCol = col;
                printf("start found at (%d,%d)\n", startRow, startCol);
            }
        }
    }
    int dirs[4][4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int dir = 0;

    data[startRow][startCol] = '.';
    pos.insert( {startRow, startCol});

    while (0 <= startRow < data.size() && 0 <= startCol < data[0].size()) {
        int nextRow = startRow + dirs[dir % 4][0], nextCol = startCol + dirs[dir%4][1];
        if ((0 > nextRow || nextRow >= data.size() || 0 > nextCol || nextCol >= data[0].size())) {
            break;
        }
        if (data[nextRow][nextCol] == '.'){
            startRow = nextRow, startCol = nextCol;
            pos.insert( {startRow, startCol});
        }
        
        else if (data[nextRow][nextCol] == '#') {
            dir += 1;
        }
    }
    ans = pos.size();

    cout << "Silver answer is " << ans << endl;
    return pos;
}

int gold(vector<vector<char> > data, std::set<std::array<int, 2>> pos, int startRow, int startCol) {
    int ans = 0;
    
    for (const auto &loc : pos) {
        data[loc[0]][loc[1]] = '#';
        //printf("Checking for cycles with (%d,%d)\n", loc[0], loc[1]);
        if (cycle_detect(data, startRow, startCol)) {
            ans += 1;
        }
        data[loc[0]][loc[1]] = '.';
    }
    
    cout << "Gold answer is " << ans << endl;
    return ans;
}


int gold_multi(vector<vector<char> > data, std::set<std::array<int, 2>> pos, int startRow, int startCol) {
  int numThreads = 4;
  std::atomic<int> globalSum(0);

  // Calculate the chunk size for each thread
  vector<array<int, 2> > pos_vec;

  for (const auto &loc : pos) {
    pos_vec.push_back({loc[0], loc[1]});
  }

  int chunkSize = pos_vec.size() / numThreads;
  std::vector<std::thread> threads;

  // Create and launch threads
  for (int i = 0; i < numThreads; ++i) {
    int start = i * chunkSize;
    int end = (i == numThreads - 1) ? pos_vec.size() : (i + 1) * chunkSize;
    
    threads.emplace_back(processArray, std::ref(data), std::ref(pos_vec), start, end, startRow, startCol, std::ref(globalSum));
  }

  // Wait for all threads to finish
  for (auto& thread : threads) {
    thread.join();
  }

  cout << "Gold answer is " << globalSum << endl;
  return globalSum;
}

void processArray(vector<vector<char>>& data, vector<array<int, 2>>& arr, int start, int end, int startRow, int startCol, std::atomic<int>& globalSum) {
  int chunkSum = 0;
  for (int i = start; i < end; i++) {
    chunkSum += processElement(data, startRow, startCol, arr[i][0], arr[i][1]);
  }
  // Atomically add the chunk's sum to the global sum
  globalSum.fetch_add(chunkSum, std::memory_order_relaxed);
}

int processElement(vector<vector<char> > data, int startRow, int startCol, int obsRow, int obsCol) {
  data[obsRow][obsCol] = '#';
  if (cycle_detect(data, startRow, startCol)) {
    return 1;
  }
  return 0;
}

bool cycle_detect(vector<vector<char> > data, int startRow, int startCol) {
    int dirs[4][4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int dir = 0;

    unordered_map<string, int> cycle_count;
    int cycle_thresh = 5;

    data[startRow][startCol] = '.';

    while (0 <= startRow < data.size() && 0 <= startCol < data[0].size()) {
        int nextRow = startRow + dirs[dir % 4][0], nextCol = startCol + dirs[dir%4][1];
        if ((0 > nextRow || nextRow >= data.size() || 0 > nextCol || nextCol >= data[0].size())) {
            break;
        }
        if (data[nextRow][nextCol] == '.'){
            startRow = nextRow, startCol = nextCol;
        }
        
        else if (data[nextRow][nextCol] == '#') {
            dir += 1;
        }
        string key = to_string(startRow) + to_string(startCol);
        if (cycle_count.find(key) != cycle_count.end()) {
            cycle_count[key] += 1;
            if (cycle_count[key] > cycle_thresh) {
                return true;
            }
        }
        else {
            cycle_count[key] = 1;
        }
    }
    return false;
}

vector<vector<char> >  parse_data(char* filename) {
    ifstream inputFile(filename); // Open file for reading

    vector<vector<char> > data;

    if (inputFile.is_open()) { 
        string line;
        while (getline(inputFile, line)) {
            std::vector<char> row(line.begin(), line.end());
            data.push_back(row);
        }
        inputFile.close(); // Close the file
    } else {
        cerr << "Error opening file." << endl;
        return data;
    }

    //for (const auto &row : data) {
    //    for (const auto &val : row) {
    //        cout << val << " ";
    //    }
    //    cout << endl;
    //}
    //cout << endl;
    
    return data;
}
