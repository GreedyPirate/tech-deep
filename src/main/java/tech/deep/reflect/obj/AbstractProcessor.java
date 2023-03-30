package tech.deep.reflect.obj;

public abstract class AbstractProcessor implements Processor{

    public void common() {
        System.out.println("common ...");
        inner();
    }

    public abstract void inner();
}
