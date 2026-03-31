use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut map = HashMap::new();        
        for num in nums {
            map.entry(num).and_modify(|entry| *entry += 1).or_insert(1);
        }
        let mut collection: Vec<(i32, i32)> = map.into_iter().collect(); 
        collection.sort_by_key(|(k, v)| *v);
        collection.into_iter().rev().take(k as usize).map(|(k, v)| k).collect()
    }
}
