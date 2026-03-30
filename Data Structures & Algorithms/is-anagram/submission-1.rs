use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut map = HashMap::new();
        for letter in s.chars() {
            map.entry(letter).and_modify(|counter| *counter += 1).or_insert(1);
        }
        for letter in t.chars() {
            if let Some(count) = map.get_mut(&letter) {
                *count -= 1;
            } else {
                return false;
            }
        }
        for value in map.into_values() {
            if value != 0 {
                return false;
            }
        }
        return true;
    }
}
