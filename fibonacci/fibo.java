package T01_14feb;

public class fibov2 {

	public static void main(String[] args) {
		
		String a="Para una variable de tipo ";
		String b=" se produce overflow con el Fibonacci numero: \t";
		String c="\t y el maximo fibonacci que puede ser almacenado es: ";
		String d="\t  y equivale al numero:  ";
		String e="  y equivale al numero:  ";
		 
		short sa = 0;
		short sb = 1;
		short stempA = 0;
		int count = 1;;
		while (sb>0) {
			stempA = sa;
			sa = sb;
			sb = (short) (sb+stempA);
			count ++;
		}
		System.out.println(a+"short"+b+count+c+(count-1)+d+sa);

		
		int ia = 0;
		int ib = 1;
		int itempA = 0;
		count = 1;
		while (ib>0) {
			itempA = ia;
			ia = ib;
			ib = ib+itempA;
			count ++;
		}
		System.out.println(a+"entero"+b+count+c+(count-1)+d+ia);
				
		long la = 0;
		long lb = 1;
		long ltempA = 0;
		count = 1;
		while (lb>0) {
			ltempA = la;
			la = lb;
			lb = lb+ltempA;
			count ++;
		}
		System.out.println(a+"long"+b+count+c+(count-1)+d+la);
				
		float fa = 0;
		float fb = 1;
		float ftempA = 0;
		count = 1;
		while (fb!= Float.POSITIVE_INFINITY) {
			ftempA = fa;
			fa = fb;
			fb = fb+ftempA;
			count ++;
		}
		System.out.println(a+"float"+b+count+c+(count-1)+d+fa);
		
		Double da = 0.0;
		Double db = 1.0;
		Double dtempA = 0.0;
		count = 1;
		while (db!=Double.POSITIVE_INFINITY) {
			dtempA = da;
			da = db;
			db = db+dtempA;
			count ++;
		}
		System.out.println(a+"Double"+b+count+c+(count-1)+e+da);
	}
	
}
