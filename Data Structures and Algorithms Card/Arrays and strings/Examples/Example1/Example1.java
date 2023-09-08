public class Example1 {
    public static void main(String[] args) {
	System.out.println(example1("racecar"));
    }

    public static boolean example1(String s) {
	for (int i = 0, j = s.length() - 1; i < j; ++i, --j) {
	    if (s.charAt(i) != s.charAt(j)) {
		return false;
	    }
	}
	return true;
    }
}

