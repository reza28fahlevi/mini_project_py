import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import ctypes

# Vertex shader source code
vertex_shader_source = """
#version 330 core
layout(location = 0) in vec3 position;
void main() {
    gl_Position = vec4(position, 1.0);
}
"""

# Fragment shader source code
fragment_shader_source = """
#version 330 core
out vec4 FragColor;
void main() {
    FragColor = vec4(0.2, 0.1, 0.65, 1.0); // Rectangle color
}
"""

def main(vertices,indices):
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a GLFW window
    window = glfw.create_window(400, 800, "OpenGL Rectangle", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Compile shaders and link them into a program
    shader = compileProgram(
        compileShader(vertex_shader_source, GL_VERTEX_SHADER),
        compileShader(fragment_shader_source, GL_FRAGMENT_SHADER)
    )

    # Generate a vertex array object (VAO), vertex buffer object (VBO), and element buffer object (EBO)
    VAO = glGenVertexArrays(1)
    VBO = glGenBuffers(1)
    EBO = glGenBuffers(1)

    # Bind the VAO
    glBindVertexArray(VAO)

    # Bind and set the VBO
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    array_type = (GLfloat * len(vertices))
    glBufferData(GL_ARRAY_BUFFER, len(vertices) * ctypes.sizeof(ctypes.c_float), array_type(*vertices), GL_STATIC_DRAW)

    # Bind and set the EBO
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    index_type = (GLuint * len(indices))
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(indices) * ctypes.sizeof(ctypes.c_uint), index_type(*indices), GL_STATIC_DRAW)

    # Define the vertex layout
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    # Unbind the VBO, VAO (not the EBO)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    # Set the background color
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Render loop
    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Use the shader program
        glUseProgram(shader)

        # Bind the VAO
        glBindVertexArray(VAO)

        # Draw the rectangle using the element array buffer (indices)
        glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, None)

        # Swap front and back buffers
        glfw.swap_buffers(window)

    # Clean up
    glDeleteVertexArrays(1, VAO)
    glDeleteBuffers(1, VBO)
    glDeleteBuffers(1, EBO)
    glDeleteProgram(shader)

    glfw.terminate()


# Vertices of the rectangle
vertices = [
    -0.5, 0.3, 0.0,
     0.5, 0.3, 0.0,
     0.5,  0.8, 0.0,
    -0.5,  0.8, 0.0
]

# Indices for the rectangle (two triangles)
indices = [
    0, 1, 2,
    2, 3, 0
]

# Vertices of the rectangle
verticess = [
    -0.5, -0.3, 0.0,
     0.5, -0.3, 0.0,
     0.5,  -0.8, 0.0,
    -0.5,  -0.8, 0.0
]

# Indices for the rectangle (two triangles)
indicess = [
    0, 1, 2,
    2, 3, 0
]

main(vertices,indices)
