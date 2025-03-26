public class po {
    public static void main(String[] args) {
        System.out.println("tamo aprendendo");

        int a = 4;
        int b = 5;
        boolean result;

        result = a < b; // true
        System.out.println("a < b: " + result);

        result = a > b; // false
        System.out.println("a > b: " + result);

        result = a <= 4; // a menor ou igual a 4 - true
        System.out.println("a <= 4: " + result);

        result = b >= 6; // b maior ou igual a 6 - false
        System.out.println("b >= 6: " + result);

        result = a == b; // a igual a b - false
        System.out.println("a == b: " + result);

        result = a != b; // a diferente de b - true
        System.out.println("a != b: " + result);

        result = a > b || a < b; // OU lógico - true
        System.out.println("a > b || a < b: " + result);

        result = 3 < a && a < 6; // E lógico - true
        System.out.println("3 < a && a < 6: " + result);

        result = !result; // NÃO lógico - false
        System.out.println("!result: " + result);
    }
}