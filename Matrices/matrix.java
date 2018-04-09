package T01_14feb;

public class matrix {

	public static void main(String[] args) {
		
		int min = 20;
		int max = 51;
		int retry = 10;
		int oper = 0;
		Double tMean = 0.0;
		Double t0 = 0.0;
		Double tf = 0.0;
		Double tt = 0.0;
		
		Double [] tMeans = new Double [max-min];
		
		for (int T=min; T<max; T++) {
			int [][] matriz1 = new int[T][T];
			int [][] matriz2 = new int[T][T];
			int [][] matriz3 = new int[T][T];
			for(int i=0; i<T; i++) {
				matriz1[i][i] = 1;
				matriz2[i][i] = 2;
				matriz3[i][i] = 0;
			}
			oper = ((T*T*T) + (T*T*(T-1)));
			
			for (int m=0; m<retry; m++) {
				t0 = (double) System.nanoTime();
				for(int i=0; i<T; i++) {
					for(int j=0; j<T; j++) {
						for(int k=0; k<T; k++) {
							matriz3[i][j] += matriz1[i][k] * matriz2[k][j];
						}
					}
				}
				tf = (double) System.nanoTime();
                tt = (double) ((tf-t0)/1000000000);
                tMean += (tt/oper);
			}
			tMeans[T-min] = (tMean/retry);
		}
		Double total =0.0;
		System.out.print("[");
		for(int i=0; i<tMeans.length; i++) {
			System.out.print(tMeans[i]+", ");
			total += tMeans[i];
		}
		System.out.println("]");
			
		tMean= (double) (total/tMeans.length);
		System.out.println("El tiempo promedio por instruccion es: " + tMean);
		
	}
}
