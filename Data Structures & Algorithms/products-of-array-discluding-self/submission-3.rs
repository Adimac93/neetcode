impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut out = Vec::new();
        for i in 0..nums.len() {
            out.push(1);
            for j in 0..nums.len() {
                if i == j {
                    continue;
                }
               out[i] *= nums[j];
            }
        }
        out
    }
}
