import java.util.*;
public class Alumno {
    private String nombre;
    private String apellido;
    private List<Integer> notas = new ArrayList<>();

    public Alumno(String nombre, String apellido, List<Integer> notas) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.notas = notas;
    }

    public Alumno() {
    }

//getters y setters

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public List<Integer> getNotas() {
        return notas;
    }

    public void setNotas(List<Integer> notas) {
        this.notas = notas;
    }

    //Metodos
    //@Override toString()

    @Override
    public String toString() {
        return "Alumno{" +
                "nombre='" + nombre + '\'' +
                ", apellido='" + apellido + '\'' +
                ", notas=" + notas +
                '}';
    }

    // calcularPromedio()
    public void calcularPromedio() {

    }

    // recibirNota()
    public void recibirNota(Integer notas) {

    }

    // listarNotas()
    public void listarNotas() {
        for (int i = 0; i < notas.size(); i++) {
            System.out.println(notas.get(i));
        }
    }
        // cantidadDeNotas
    public void cantidadDeNotas() {
        System.out.println(notas.size());
    }

}
