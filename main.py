from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.image import Image
from molov import detect_objects

Builder.load_file("myapp.kv")

class FileLoader(BoxLayout):
    def upload_file(self):
        # Dosya seçimini al
        selected_file = self.ids.filechooser.selection
        if selected_file:
            source_file = selected_file[0]

            # Nesne algılama işlemini yap

            output_image = detect_objects(source_file)
            output_image = "output_image.jpg"
            if output_image:
                self.ids.label.text = "görsel basarıyla kaydedildi"
                self.show_image(output_image)
                # Algılanan görseli göster
            else:
                self.ids.label.text = "Hiçbir nesne algılanamadı."
        else:
            self.ids.label.text = "No file selected."

    def show_image(self, image_path):
        """
        İşlenmiş görseli Kivy arayüzünde gösterir.
        """
        self.ids.image_container.clear_widgets()
        image_widget = Image(source=str(image_path))
        self.ids.image_container.add_widget(image_widget)

class FileUploadApp(App):
    def build(self):
        return FileLoader()

if __name__ == '__main__':
    FileUploadApp().run()

