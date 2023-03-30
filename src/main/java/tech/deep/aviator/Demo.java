package tech.deep.aviator;

import com.googlecode.aviator.AviatorEvaluator;
import com.googlecode.aviator.Expression;

import java.io.IOException;

public class Demo {
    public static void main(String[] args) throws IOException {
        Expression expression = AviatorEvaluator.getInstance().compileScript("av/hello.av");
        expression.execute();
    }
}
