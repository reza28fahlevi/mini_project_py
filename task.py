import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

# Shader source code
vertex_shader_src = """
#version 330 core
layout (location = 0) in vec3 aPos;
void main()
{
    gl_Position = vec4(aPos, 1.0);
}
"""

fragment_shader_src = """
#version 330 core
out vec4 FragColor;
void main()
{
    FragColor = vec4(0.75, 0.2, 0.2, 1.0); // Shapes color
}
"""

# Vertex data for a rectangle, line, and triangle
vertices = [
    # Rectangle (two triangles)
    -0.75, -0.25, 0.0,
    -0.75, 0.25, 0.0,
    -0.25, 0.25, 0.0,
    -0.25, -0.25, 0.0,
    
    # Line
    -0.75,  0.75, 0.0,
     0.75,  0.25, 0.0,

    # Triangle
     -0.0, -0.25, 0.0,
     0.5, -0.25, 0.0,
     0.25,  0.25, 0.0,

    # Line 1
    -0.75,  -0.75, 0.0,
    -0.25,  -0.35, 0.0,
    # Line 2
    -0.75,  -0.35, 0.0,
    -0.25,  -0.75, 0.0,
]

indices = [
    # Rectangle
    0, 1, 2,
    2, 3, 0,

    # Line
    4, 5,

    # Triangle
    6, 7, 8,

    # X
    9,10,
    11,12
]

def main():
    # Initialize GLFW
    if not glfw.init():
        return
    
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 800, "OpenGL Shapes", None, None)
    if not window:
        glfw.terminate()
        return
    
    # Make the window's context current
    glfw.make_context_current(window)

    # Compile shaders and link them into a program
    shader_program = compileProgram(
        compileShader(vertex_shader_src, GL_VERTEX_SHADER),
        compileShader(fragment_shader_src, GL_FRAGMENT_SHADER)
    )

    # Generate and bind a Vertex Array Object
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    # Generate and bind a Vertex Buffer Object
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, len(vertices) * 4, (GLfloat * len(vertices))(*vertices), GL_STATIC_DRAW)

    # Generate and bind an Element Buffer Object
    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(indices) * 4, (GLuint * len(indices))(*indices), GL_STATIC_DRAW)

    # Specify the layout of the vertex data
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    # Unbind the VBO and VAO
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    # Set the background color
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Main loop
    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # Draw the shapes
        glUseProgram(shader_program)
        glBindVertexArray(VAO)
        
        # Draw rectangle
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, ctypes.c_void_p(0))
        
        # Draw line
        glDrawElements(GL_LINES, 2, GL_UNSIGNED_INT, ctypes.c_void_p(6 * 4))
        
        # Draw triangle
        glDrawElements(GL_TRIANGLES, 3, GL_UNSIGNED_INT, ctypes.c_void_p(8 * 4))

        # Draw X
        glDrawElements(GL_LINES, 2, GL_UNSIGNED_INT, ctypes.c_void_p(11 * 4))
        glDrawElements(GL_LINES, 2, GL_UNSIGNED_INT, ctypes.c_void_p(13 * 4))
        
        glBindVertexArray(0)
        glUseProgram(0)

        # Swap front and back buffers
        glfw.swap_buffers(window)
    
    # Cleanup
    glDeleteVertexArrays(1, [VAO])
    glDeleteBuffers(1, [VBO])
    glDeleteBuffers(1, [EBO])
    glDeleteProgram(shader_program)

    glfw.terminate()

if __name__ == "__main__":
    main()
