impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut out = String::new();
        for word in strs {
            out.push_str(&format!("{}#{}", word.len(), word));
        }
        out
    }

    pub fn decode(s: String) -> Vec<String> {
        let mut i = 0;
        let mut out = Vec::new();
        let chars: Vec<char> = s.chars().collect();
        while i < s.len() {
            let mut buf = String::new();
            while chars[i] != '#' {
                buf.push(chars[i]);
                i += 1;
            } 
            i += 1;
            
            println!("buf: {buf}");
            let num: i32 = buf.parse().unwrap();
            let mut word = String::new();
            
            for j in i..i+num as usize {
                word.push(chars[j]);
            }
            i += num as usize;
            out.push(word);
        }
        out
    }
}
