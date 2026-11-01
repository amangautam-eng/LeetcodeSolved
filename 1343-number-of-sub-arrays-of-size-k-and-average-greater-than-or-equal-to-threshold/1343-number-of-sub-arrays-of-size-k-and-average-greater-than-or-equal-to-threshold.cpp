class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int total=arr[0],cnt=0;
        int l=0,r=0;
        int n=arr.size();
        while(r<k-1){
            r++;
            total+=arr[r];
        }
        if(total/k >= threshold){
            cnt++;
        }
        while(r<n-1){
            r++;
            total+=arr[r];
            total-=arr[l];
            l++;

            if (total/k >= threshold){
                cnt++;
            }
        }
        return cnt;
    }
};