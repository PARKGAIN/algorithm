public class Main {
	public static void main(String[] args) {
		int N =30,sum = 0,B = 10,C= 20;
		int[] arr= new int[N];
		for (int i = 0; i < N; i++) {
			sum += arr[i];
		}
		 int result = N+(N-B)/C;
		 System.out.println(result);
	}
}
