#include <iostream>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            for (int i = 0; i < nums.size(); i++){
                for (int j = i + 1; j < nums.size(); j++){
                    if (nums[i] + nums[j] == target){
                        return {i, j};
                    }
                }
            }
            return {};

        }
    };


int main(void) {
    Solution solution;
    vector<int> numbers;
    int input;
    cout << "Input numbers: n > 0: Type -1 to stop" << endl;
    while(cin >> input && input != -1 ){
        numbers.push_back(input);

    }
    int targer;
    cout << "Target Number: ";
    cin >> targer;
    vector<int> indices = solution.twoSum(numbers, targer);  
    cout << "Indices are: {" << indices[0] <<", " << indices[1] << "} ";    

}
