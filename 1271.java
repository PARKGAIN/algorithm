import java.util.Scanner;

public class Main1271 {
	public static void main(String[] args) {
		/* int n = 1000, m = 100; */
		/*
		 * System.out.println(n/m); 
		 * System.out.println(n%m);
		 */
		
		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(sc.nextLine());
		int m = Integer.parseInt(sc.nextLine());
		
		System.out.println(n/m);
		System.out.println(n%m);
	}
}


//엄청난 부자2 라는 제목의 문제로 n이라는 액수의 돈을 m명의 사람들에게 똑같이 분배하고 남은 돈도 계산하는 문제이다.
