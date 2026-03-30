use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<[usize; 26], Vec<String>> = HashMap::new();
        for word in strs {
            let mut signature = [0; 26]; 
            for letter in word.chars() {
                signature[letter as usize - 97] += 1;
            }
            map.entry(signature).and_modify(|entry| entry.push(word.clone())).or_insert(vec![word]);
        }
        return map.into_values().collect();
    }
}
