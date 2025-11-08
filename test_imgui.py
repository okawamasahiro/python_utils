import glfw
import OpenGL.GL as gl
import imgui
from imgui.integrations.glfw import GlfwRenderer

def main():
    # === GLFW初期化 ===
    if not glfw.init():
        print("GLFW初期化失敗")
        return

    window = glfw.create_window(800, 600, "pyimgui Sample", None, None)
    glfw.make_context_current(window)

    # === ImGui初期化 ===
    imgui.create_context()
    impl = GlfwRenderer(window)

    # === メインループ ===
    while not glfw.window_should_close(window):
        glfw.poll_events()
        impl.process_inputs()

        imgui.new_frame()

        # === UI ===
        imgui.begin("Test Window")
        imgui.text("PyImGuiは動作しています！")
        if imgui.button("クリック"):
            print("ボタンが押されました")
        imgui.end()

        # === 描画 ===
        gl.glClearColor(0.1, 0.1, 0.1, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        imgui.render()
        impl.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    impl.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    main()