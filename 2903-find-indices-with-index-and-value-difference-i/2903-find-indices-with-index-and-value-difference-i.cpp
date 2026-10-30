class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
       vector<int> arr={-1,-1};
        int n = nums.size();
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if ((abs(i-j) >= indexDifference) && (abs(nums[i]-nums[j]) >= valueDifference)){
                    arr[0]=i;
                    arr[1]=j;
                    return arr;
                }
            }
        }
        return arr;

    } 
};