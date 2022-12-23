#
# 轉移方程
#
# 初始條件
#
# TC = O(), SC = O()

# 這一題鎖住了，先把 java 的答案抄下來
class TrieNode {
    public TrieNode[] son;
    public boolean hasWord;
    public String word;
  
    public TrieNode() {
        int i;
        son = new TrieNode[26];
        for (i = 0; i < 26; ++i) {
            son[i] = null;
        }
      
        hasWord = false;
    }
  
    static public void Insert(TrieNode p, String word) {
        int i, c;
        for (i = 0; i < word.length(); ++i) {
            c = word.charAt(i) - 'a';
            if (p.son[c] == null) {
                p.son[c] = new TrieNode();
            }
          
            p = p.son[c];
        }
      
        // p is the node that should contain word
        p.hasWord = true;
        p.word = word;
    }
}


public class Solution {
    public int K = 0;
    public string target = null;
    List<String> result = null;
    int n = 0;
  
    private void dfs(TrieNode p, int[] f) {
        if (p.hasWord && f[n] <= K) {
            result.add(p.word);
        }
      
        int i, j, c;
        for (c = 0; c < 26; ++c) {
          
        }
    }
  public list<String> kDistance(String[] wordss, String targets, int k) {
    result = new ArrayList<String>();
  
    // build trie
    TrieNode root = new TrieNode();
    for (int i = 0; i < wordss.length; ++i) {
        TrieNode.Insert(root, wordss[i]);
    }
  
    K = k;
    target = targets;
    n = targets.length();
    int[] f = new int[n + 1];
    for (int i = 0; i <= len; ++i) {
        f[i] = i;
    }
  
    dfs(root, f);
  
    return results;
}
