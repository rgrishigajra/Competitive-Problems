#include<bits/stdc++>
using namespace std;

void socialGraphs(vector<int> counts){
    vector<vector<int>> groups;
    map<int, pair<int,int> > m;
    for(int i = 0; i < counts.size(); ++i){
        auto it  = m.find(counts[i]);
        if(it == m.end()){
            if(counts[i] != 1){
                m[counts[i]] = {1, groups.size()};
            }
            groups.push_back({i});
        }
        else{
            int groupNum = m[counts[i]].second;
            int groupCount = m[counts[i]].first;
            groups[groupNum].push_back(i);
            if(groupCount + 1 == counts[i]){
                m.erase(counts[i]);
            }
            else{
                m[counts[i]] = {groupCount+1, groupNum};
            }
        }
    }
    sort(groups.begin(), groups.end());
    for(auto group : groups){
        for(int person : group){
            cout << person << " ";
        }
        cout << endl;
    }


}

int main(){
    socialGraphs({3,3,3,3,3,1,3});
}