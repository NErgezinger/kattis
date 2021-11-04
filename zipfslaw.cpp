#include <iostream>
#include <map>
#include <utility>
#include <regex>

using namespace std;

int main() {

    int n;
    bool new_case = false;
    bool there_was_word;
    map<string,int> word_counts;
    vector<string> word_list;
    regex re ("[a-zA-Z]+");
    smatch match;
    string word;

    cin >> n;

    string line;
    while (getline(cin, line)) {
        if (new_case) {
            if (line.size() > 0) {
                cout << endl;
                n = stoi(line);
                new_case = false;
                word_counts.clear();
            }
        }

        else if (line == "EndOfText") {
                there_was_word = false;
                for (pair<string, int> word_count: word_counts) {
                    if (word_count.second == n) {
                        word_list.push_back(word_count.first);
                        there_was_word = true; 
                    }
                }
                if (!there_was_word) {
                    cout << "There is no such word." << endl;
                } else {
                    sort(word_list.begin(), word_list.end());
                    for (string s: word_list) cout << s << endl;
                }
                word_list.clear();
                new_case = true;
            }

        else {
            while (regex_search(line, match, re)) {
                word = "";
                for (char c: (string) match[0]) {
                    word.push_back(tolower(c));
                }
                word_counts[word] += 1;
                line = match.suffix();
            }
        }
    }


    return 0;
}