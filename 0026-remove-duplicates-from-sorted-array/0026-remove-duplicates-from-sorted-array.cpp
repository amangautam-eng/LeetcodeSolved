class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left=0,right=0,n=nums.size(),cnt=1;
        while(right<n){
            if(nums[left]==nums[right]){
                right++;
            }
            else{
                left++;
                swap(nums[left],nums[right]);
                cnt++;
                right++;
            }
        }
        return cnt;

    }
};