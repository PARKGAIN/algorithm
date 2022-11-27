
### 자바 풀이 (212ms)
```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int A = scanner.nextInt();
		int B = scanner.nextInt();
		System.out.println(A+B);
        scanner.close();
	}
}


```

###### 숫자 입력이기 때문에 Scanner클래스 말고  int A = System.in.read() - 48; 이렇게 작성하면 더 빠름

### node.js 풀이(124ms)
```javascript
const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);
let b = parseInt(input[1]);
console.log(a+b);

```

######  readline() 은 비동기이고 readFileSync()는 동기이다.
