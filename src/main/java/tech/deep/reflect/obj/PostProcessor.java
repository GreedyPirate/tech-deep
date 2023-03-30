package tech.deep.reflect.obj;

@Consistent
public class PostProcessor implements Processor{

    private String name;

    @Override
    public void process() {
        System.out.println("post process");
    }
}
