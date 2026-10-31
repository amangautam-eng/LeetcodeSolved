class RandomizedSet {
private:
    set<int> numbers;
public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        auto it = numbers.find(val);
        if (it!=numbers.end()){
            return false;
        }
        else{
            numbers.insert(val);
            return true;
        }
        
    }
    
    bool remove(int val) {
        auto it=numbers.find(val);
        if(it!=numbers.end()){
            numbers.erase(val);
            return true;
        }
        else{
            return false;
        }
        
    }
    
    int getRandom() {
        int x=rand()%numbers.size();
        auto it=numbers.begin();
        advance(it,x);
        return *it;
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */