import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double A = sc.nextDouble();
		double B = sc.nextDouble();
		System.out.println(A/B);
		sc.close();
		// 처음에 int로 했더니 안됨 double로 해야함
	}
}
