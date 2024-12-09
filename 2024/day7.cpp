#include <bits/stdc++.h>
#include <string>
#include <regex>


using namespace std;

struct Node {
  int val;
  Node* left;
  Node* right;
   
  Node(int x) : val(x), left(NULL), right(NULL) {}
};

typedef vector<vector<int> > vvi;

vvi parse_data(char* filename);
void silver(vvi &data);
Node* create_graph(vector<int> line, int index);
void printNode(const Node *node);
void printTree(Node *root);
void gold(vvi &data);

int main(int argc, char* argv[]) {
    int initRow = 0, initCol = 0;
    vvi data = parse_data(argv[1]);
    silver(data);
    gold(data);

    return 0;
}

vvi parse_data(char* filename) {
    ifstream inputFile(filename); // Open file for reading

    vvi data;

    if (inputFile.is_open()) { 
        string line;
        while (getline(inputFile, line)) {
          istringstream iss(line);
          int num;
          vector<int> row;

          while (iss >> num) {
            row.push_back(num);
          }
          if (!row.empty()) {
            data.push_back(row);
          }
        }
        inputFile.close(); // Close the file
    } else {
        cerr << "Error opening file." << endl;
        return data;
    }

    for (auto row : data) {
      for (auto val : row) {
        cout << val << " ";
      }
      cout << endl;
    }
    return data;
}

void silver(vvi &data) {
  int ans = 0;

  vector<int> line = {1,2,3};

  Node *test = create_graph(line, 1);

  printTree(test);

  //for (int i = 0; i < data.size(); i++) {
  //  cout << "SIZE " << data[i].size() << endl;
  //  Node root = create_graph(data[i]);
  //  printNode(root);
  //}
}

Node* create_graph(vector<int> line, int index) {

  if (index >= line.size()) return new Node(line[0]);

  Node* root = new Node(line[0]);

  // Create left child with addition
  root->left = new Node(root->val + line[index]);
  root->left->left = create_graph(line, index + 1);
  
  // Create right child with multiplication
  root->right = new Node(root->val * line[index]);
  root->right->right = create_graph(line, index + 1);
  
  return root;
}

void printNode(const Node *node) {
  cout << "Value: " << node->val << " Left: " << node->left << " Right " << node->right << endl;
}

void printTree(Node *root) {
  if (root != NULL) {
    printTree(root->left);
    printNode(root);
    printTree(root->right);
  }
}

void gold(vvi &data) {

}