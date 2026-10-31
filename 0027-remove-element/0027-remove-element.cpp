class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n=nums.size();
        if (n==0) return 0;
        int left=0,right=n-1,cnt=0;

        while(left<right){
            while(right>=0 && nums[right]==val){
                right--;
            }
            if(right>left && nums[left]==val){
                swap(nums[left],nums[right]);
                left++;
            }
            else{
                left++;
            }
        }
        for(int i=0;i<n;i++){
            if (nums[i]!=val) cnt++;

        }
        return cnt;
    }
};