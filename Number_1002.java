package beakjoon;

import java.util.Scanner;

public class Number_1002 {

public static int getCircleequation(int x1,int x2,int y1,int y2,int r1,int r2) {
		int distance = (int)(Math.pow(x1 + x2, 2)) + (int)(Math.pow(r1+r2, 2));
		
		if(x1==x2 && y1==y2 && r1==r2) return -1;
		
		int sum_radius = (int)(Math.pow(r1+r2,2));
		int sub_radius = (int)(Math.pow(r2-r1,2));
		if(distance>sum_radius) {
			return 0;
		}else if(distance<sub_radius) {
			return 0;
		}else if(distance==sub_radius) {
			return 1;
		}else if(distance==sum_radius) {
			return 1;
		}else {
			return 2;
		}	
}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int test_case = sc.nextInt();
		
		for(int i=0; i<test_case; i++) {
				int gyuhyon_x1coordinate = sc.nextInt();
				int gyuhyon_y1coordinate = sc.nextInt();
				int gyuhyon_calculation = sc.nextInt();
				
				int senghwan_x2coordinate = sc.nextInt();
				int senghwan_y2coordinate = sc.nextInt();
				int senghwan_calculation = sc.nextInt();
				
				getCircleequation(gyuhyon_x1coordinate, senghwan_x2coordinate, gyuhyon_y1coordinate, senghwan_y2coordinate, gyuhyon_calculation,senghwan_calculation);
		}
		sc.close();
	}

}
