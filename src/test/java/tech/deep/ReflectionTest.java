package tech.deep;

import org.junit.jupiter.api.Test;
import org.reflections.Reflections;
import tech.deep.reflect.obj.Processor;

import java.lang.reflect.Modifier;
import java.util.Set;

public class ReflectionTest {

    @Test
    public void testClass() {
        Reflections ref = new Reflections("tech.deep.reflect.obj");
        Set<Class<? extends Processor>> processImps = ref.getSubTypesOf(Processor.class);
        for (Class<? extends Processor> imp : processImps) {
            if (Modifier.isAbstract(imp.getModifiers())) {
                System.out.println("found abstract");
            }
            System.out.println(imp.getSimpleName());
        }
    }
}
