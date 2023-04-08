import bpy
import math

# Создаем 3 сферы
for i in range(3):
    bpy.ops.mesh.primitive_uv_sphere_add(location=(i*2, 0, 0))

# Анимация каждой сферы
for i, obj in enumerate(bpy.context.scene.objects):
    if obj.type == 'MESH':
        # Устанавливаем кадры начала и конца анимации
        bpy.context.scene.frame_start = 0
        bpy.context.scene.frame_end = 250

        # Вращаем каждую сферу вокруг Y-оси по окружности
        for frame in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end):
            # Вычисляем угол вращения для текущего кадра
            angle = math.radians(frame * 4 + i * 120)

            # Устанавливаем позицию сферы на текущем кадре
            obj.location.x = 2 * math.sin(angle)
            obj.location.y = 2 * math.cos(angle)

            # Добавляем ключевой кадр для позиции сферы
            obj.keyframe_insert(data_path='location', frame=frame)