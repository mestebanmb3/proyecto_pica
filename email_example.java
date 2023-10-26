import org.apache.commons.jexl3.*;

public class EmailTrigger {
    public static void main(String[] args) {
        // Supongamos que 'data' es el objeto de datos que contiene la lectura de humedad
        double humedad = data.getHumedad();

        // Configurar el motor JEXL
        JexlEngine jexl = new JexlBuilder().create();
        JexlContext context = new MapContext();

        // Agregar la variable 'humedad' al contexto
        context.set("humedad", humedad);

        // Definir la expresión condicional
        String condition = "humedad > 65";

        // Evaluar la expresión
        JexlExpression expr = jexl.createExpression(condition);
        boolean resultado = (boolean) expr.evaluate(context);

        // Si el resultado es verdadero, enviar el correo electrónico
        if (resultado) {
            // Lógica para enviar el correo electrónico aquí
        }
    }
}