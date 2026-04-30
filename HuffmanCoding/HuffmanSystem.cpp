#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

// 哈夫曼树结点结构
struct HTNode {
    char data;
    double weight;
    int parent, lchild, rchild;
    HTNode() : data(' '), weight(0), parent(-1), lchild(-1), rchild(-1) {}
};

struct HCode {
    char data;
    string code;
};

class HuffmanSystem {
private:
    vector<HTNode> ht;
    vector<HCode> hcd;
    int n;

public:
    void SelectMin(int range, int& s1, int& s2) {
        double min1 = 1e9, min2 = 1e9;
        s1 = -1; s2 = -1;
        for (int i = 0; i < range; i++) {
            if (ht[i].parent == -1) {
                if (ht[i].weight < min1) {
                    min2 = min1; s2 = s1;
                    min1 = ht[i].weight; s1 = i;
                } else if (ht[i].weight < min2) {
                    min2 = ht[i].weight; s2 = i;
                }
            }
        }
    }

    void CreateTree(const vector<char>& chars, const vector<double>& weights) {
        n = chars.size();
        ht.assign(2 * n - 1, HTNode());
        for (int i = 0; i < n; i++) {
            ht[i].data = chars[i];
            ht[i].weight = weights[i];
        }
        for (int i = n; i < 2 * n - 1; i++) {
            int s1, s2;
            SelectMin(i, s1, s2);
            ht[s1].parent = i; ht[s2].parent = i;
            ht[i].lchild = s1; ht[i].rchild = s2;
            ht[i].weight = ht[s1].weight + ht[s2].weight;
        }
        // 生成编码
        hcd.clear();
        for (int i = 0; i < n; i++) {
            string temp = "";
            int curr = i, p = ht[curr].parent;
            while (p != -1) {
                temp += (ht[p].lchild == curr) ? '0' : '1';
                curr = p; p = ht[curr].parent;
            }
            reverse(temp.begin(), temp.end());
            hcd.push_back({ht[i].data, temp});
        }
    }

    void ShowTable() {
        cout << "\n[哈夫曼编码表]" << endl;
        cout << "-------------------" << endl;
        cout << "字符\t权重\t编码" << endl;
        for (int i = 0; i < n; i++) {
            cout << ht[i].data << "\t" << ht[i].weight << "\t" << hcd[i].code << endl;
        }
        cout << "-------------------" << endl;
    }

    string Encode(string text) {
        string res = "";
        for (char c : text) {
            for (auto& item : hcd) if (item.data == c) res += item.code;
        }
        return res;
    }

    string Decode(string code) {
        string res = "";
        int curr = ht.size() - 1;
        for (char bit : code) {
            if (bit == '0') curr = ht[curr].lchild;
            else if (bit == '1') curr = ht[curr].rchild;
            else continue;

            if (ht[curr].lchild == -1 && ht[curr].rchild == -1) {
                res += ht[curr].data;
                curr = ht.size() - 1;
            }
        }
        return res;
    }
};

void PrintMenu() {
    cout << "\n===== 哈夫曼编译码系统 =====" << endl;
    cout << "1. 初始化(输入字符与权值)" << endl;
    cout << "2. 文本编码(Text -> 0101)" << endl;
    cout << "3. 序列译码(0101 -> Text)" << endl;
    cout << "0. 退出系统" << endl;
    cout << "============================" << endl;
    cout << "请选择操作: ";
}

int main() {
    HuffmanSystem sys;
    int choice;
    bool initialized = false;

    while (true) {
        PrintMenu();
        if (!(cin >> choice)) break;

        if (choice == 0) break;
        switch (choice) {
            case 1: {
                int num;
                cout << "输入字符数量: "; cin >> num;
                vector<char> c(num); vector<double> w(num);
                cout << "请依次输入 字符 权重 (例如 A 10):" << endl;
                for (int i = 0; i < num; i++) cin >> c[i] >> w[i];
                sys.CreateTree(c, w);
                sys.ShowTable();
                initialized = true;
                break;
            }
            case 2: {
                if (!initialized) { cout << "请先执行初始化！" << endl; break; }
                string text; cout << "输入待编码字符串: "; cin >> text;
                cout << "编码结果: " << sys.Encode(text) << endl;
                break;
            }
            case 3: {
                if (!initialized) { cout << "请先执行初始化！" << endl; break; }
                string code; cout << "输入二进制序列: "; cin >> code;
                cout << "译码结果: " << sys.Decode(code) << endl;
                break;
            }
            default: cout << "无效选择" << endl;
        }
        system("pause"); // Windows专用：防止界面直接跳过
        system("cls");   // 清屏，让演示更整洁
    }
    return 0;
}
