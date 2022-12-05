import java.util.*;

public class Profe {
    private String nombre;
    private String apellido;
    private List<Alumno> alumnos = new ArrayList<>();

    public Profe() {
    }

    public Profe(String nombre, String apellido, List<Alumno> alumnos) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.alumnos = alumnos;
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

    public List<Alumno> getAlumnos() {
        return alumnos;
    }

    public void setAlumnos(List<Alumno> alumnos) {
        this.alumnos = alumnos;
    }

    //METODOS
    // aniadirAlumno()
    public void aniadirAlumno(Alumno alumno){
        alumnos.add(alumno);
    }
    // eliminarAlumno(){
    public void eliminarAlumno( int id ){
        for (int i = 0; i  > alumnos.size(); i++){
            if (i == id){
                alumnos.remove(id);
                System.out.println("Se removió el alumno con exito");
            }
        }
    }
    // buscarAlumno()
    public void buscarAlumno(int id){
        for(int i = 0; i < alumnos.size() ;i++){
            if (i == id) {
                System.out.println(alumnos.get(i));
                System.out.println("Se encontro el alumno buscado");
            }
        }

    }
    // listaralumnos()
    public void listaralumnos(){
        for(int i = 0; i < alumnos.size() ;i++){
            System.out.println(alumnos.get(i));
        }
    }
    // cantidadAlumnos()
    public void cantidadAlumnos(){
        System.out.println(alumnos.size());
    }

}
