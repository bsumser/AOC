#include <bits/stdc++.h>
#include <chrono>
#include <string>

using namespace std;

int silver(vector<vector<char> > data);
int gold(vector<vector<char> > data);
vector<vector<char> > parse_data(char* filename);

int main(int argc, char* argv[]) {

    vector<vector<char> > data = parse_data(argv[1]);
    silver(data);
    gold(data);

    return 0;
}

int silver(vector<vector<char> > data) {
    auto start = std::chrono::high_resolution_clock::now();
    int ans = 0;

    int startRow = 0;
    int startCol = 0;

    std::set<std::array<int, 2>> pos;
    
    for (int row = 0; row < data.size(); row++) {
        for (int col = 0; col < data[0].size(); col++) {
            if (data[row][col] == '^') {
                startRow = row, startCol = col;
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

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    cout << "Silver done in " << duration.count() << " microseconds" << endl;
    cout << "Silver answer is " << ans << endl;
    return ans;
}

int gold(vector<vector<char> > data) {
    auto start = std::chrono::high_resolution_clock::now();
    int ans = 0;
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    cout << "Gold done in " << duration.count() << " microseconds" << endl;
    return ans;
}

vector<vector<char> >  parse_data(char* filename) {
    auto start = std::chrono::high_resolution_clock::now();
    ifstream inputFile(filename); // Open file for reading

    vector<vector<char> > data;

    if (inputFile.is_open()) { 
        string line;
        while (getline(inputFile, line)) {
            cout << line << endl; // Read and output each line
            std::vector<char> row(line.begin(), line.end());
            data.push_back(row);
        }
        inputFile.close(); // Close the file
    } else {
        cerr << "Error opening file." << endl;
        return data;
    }

    for (const auto &row : data) {
        for (const auto &val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    cout << endl;
    
    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    
    cout << "Parsing done in " << duration.count() << " microseconds" << endl;

    return data;
}