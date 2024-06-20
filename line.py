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
    FragColor = vec4(1.0, 1.0, 1.0, 1.0); // White color
}
"""

# Vertices of the line
vertices = [
    -0.5, 0.0, 0.0,  # Start point of the line
     0.5, 0.0, 0.0   # End point of the line
]

def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a GLFW window
    window = glfw.create_window(800, 600, "OpenGL Line", None, None)
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

    # Generate a vertex buffer object (VBO) and vertex array object (VAO)
    VBO = glGenBuffers(1)
    VAO = glGenVertexArrays(1)

    # Bind the VAO
    glBindVertexArray(VAO)

    # Bind the VBO and upload the vertex data
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    array_type = (GLfloat * len(vertices))
    glBufferData(GL_ARRAY_BUFFER, len(vertices) * ctypes.sizeof(ctypes.c_float), array_type(*vertices), GL_STATIC_DRAW)

    # Define the vertex layout
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    # Unbind the VBO and VAO
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    # Set the background color
    glClearColor(0.0, 0.0, 0.0, 1.0)

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

        # Draw the line
        glDrawArrays(GL_LINES, 0, 2)

        # Swap front and back buffers
        glfw.swap_buffers(window)

    # Clean up
    glDeleteVertexArrays(1, VAO)
    glDeleteBuffers(1, VBO)
    glDeleteProgram(shader)

    glfw.terminate()

if __name__ == "__main__":
    main()
