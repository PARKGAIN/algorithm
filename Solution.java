public class Solution {
	public static void main(String[] args) {
		
		for (String string : args) {
			
		}
		int sum= 0;
		int[] numbers = {};
		for(int i=0; i<10; i++) {
			
			sum += i;
		}
		System.out.println(sum);
		
		Solution sol = new Solution();
		
		sol.solution(numbers);
		
	}
	
	public int solution(int[] numbers) {
		int sum2= 0;
		for (int i = 0; i < numbers.length; i++) {
			sum2 += numbers[i];
		}
		return sum2;
	}
	
	
	
	
}
