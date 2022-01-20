import pygame

from hints import icons_sprite, Hints
from stats import Stats, stats_sprite
from dialog import ramka_sprite, Dialog
from map_static import map_sprite
from support import import_csv_layout, import_cut_graphic
from settings import tile_size
from tiles import AnimatedTile, CharacterTile, StaticTile, list_spawn_pos
from khan import Khan, khan_sprite

khan = Khan()
dialog = Dialog()
stats = Stats()


def create_tile_group(layout, type):
    sprite_group = pygame.sprite.Group()
    for row_index, row in enumerate(layout):
        for col_index, val in enumerate(row):
            if val != '-1':
                x = col_index * tile_size
                y = row_index * tile_size
                if type == 'animation_forest':
                    sprite = AnimatedTile(tile_size, x, y, '../graphics/forest/Tree', 0.15)
                    print(x, y, 'forest')
                    sprite_group.add(sprite)
                if type == 'farm_forest':
                    sprite = AnimatedTile(tile_size, x, y, '../graphics/forest/Tree_Stump', 0.15)
                    print(x, y, 'cut')
                    sprite_group.add(sprite)
                if type == 'animation_water_left_bottom':
                    sprite = AnimatedTile(tile_size, x, y, '../graphics/anim water/River_Bottom_Left', 0.18)
                    sprite_group.add(sprite)
                if type == 'animation_water_right_bottom':
                    sprite = AnimatedTile(tile_size, x, y, '../graphics/anim water/River_Bottom_Left — miror', 0.18)
                    sprite_group.add(sprite)
                if type == 'animation_water_left_up':
                    sprite = AnimatedTile(tile_size, x, y, '../graphics/anim water/River_Top_Left', 0.18)
                    sprite_group.add(sprite)
                if type == 'animation_water_right_up':
                    sprite = AnimatedTile(tile_size, x, y, '../graphics/anim water/River_Top_Left — miror', 0.18)
                    sprite_group.add(sprite)
                if type == 'people':
                    sprite = CharacterTile(tile_size, x, y, '../graphics/npc', 0.12)
                    Hints((x + 8, y - 20))
                    sprite_group.add(sprite)
                if type == 'house':
                    water_list = import_cut_graphic('../graphics/hous/Слой 2.png')
                    tile_surface = water_list[int(val)]
                    sprite = StaticTile(tile_size, x, y, tile_surface)
                    sprite_group.add(sprite)

    return sprite_group


class Map:
    def __init__(self, map_data):
        # импортирование положения и спрайтов лошадей
        self.farm_flag = None
        test_layout = import_csv_layout(map_data['лошади'])
        self.horse_sprites = create_tile_group(test_layout, 'лошади')

        house_layout = import_csv_layout(map_data['house'])
        self.house_sprites = create_tile_group(house_layout, 'house')

        # импортирование положения и спрайтов дервьев
        forest_layout = import_csv_layout(map_data['animation_forest'])
        self.forest_sprites = create_tile_group(forest_layout, 'animation_forest')
        self.forest_farm_sprites = create_tile_group(forest_layout, 'farm_forest')

        # импортирование положения и спрайтов кусков озера
        anim_water_layout_1 = import_csv_layout(map_data['animation_water_left_bottom'])
        self.anim_water_sprites_1 = create_tile_group(anim_water_layout_1, 'animation_water_left_bottom')
        anim_water_layout_2 = import_csv_layout(map_data['animation_water_right_bottom'])
        self.anim_water_sprites_2 = create_tile_group(anim_water_layout_2, 'animation_water_right_bottom')
        anim_water_layout_3 = import_csv_layout(map_data['animation_water_left_up'])
        self.anim_water_sprites_3 = create_tile_group(anim_water_layout_3, 'animation_water_left_up')
        anim_water_layout_4 = import_csv_layout(map_data['animation_water_right_up'])
        self.anim_water_sprites_4 = create_tile_group(anim_water_layout_4, 'animation_water_right_up')

        # импортирование положения и спрайтов жителей
        npc_layout = import_csv_layout(map_data['people'])
        self.npc_sprites = create_tile_group(npc_layout, 'people')

        self.map_sprite = map_sprite
        self.khan_sprite = khan_sprite
        self.ramka_sprite = ramka_sprite
        self.stats_sprite = stats_sprite
        self.icons_sprite = icons_sprite
        self.icon_flag = False
        self.one_icon = pygame.sprite.Group()
        self.cut_forest = pygame.sprite.Group()
        self.dialog_num = None
        self.khan_view = 'top'
        self.farm_tree = None
        self.flag_action = False

    def run(self, surface, interface,
            cam_x, cam_y, cam_zoom_x, cam_zoom_y,
            khan_view, khan_x, khan_y,
            flag_action, dialog_part):

        self.khan_view = khan_view
        self.map_sprite.draw(surface)
        self.flag_action = flag_action

        self.horse_sprites.draw(surface)
        self.horse_sprites.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)

        self.anim_water_sprites_1.draw(surface)
        self.anim_water_sprites_2.draw(surface)
        self.anim_water_sprites_3.draw(surface)
        self.anim_water_sprites_4.draw(surface)
        self.anim_water_sprites_1.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)
        self.anim_water_sprites_2.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)
        self.anim_water_sprites_3.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)
        self.anim_water_sprites_4.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)

        self.khan_sprite.draw(surface)
        self.khan_sprite.update(khan_view, khan_x, khan_y)

        self.cut_forest.draw(surface)
        self.cut_forest.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)
        self.forest_farm_sprites.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)
        self.forest_sprites.draw(surface)
        self.forest_sprites.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)

        self.house_sprites.draw(surface)
        self.house_sprites.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)

        self.npc_sprites.draw(surface)
        self.npc_sprites.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)
        self.icons_sprite.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)

        self.map_sprite.update(cam_x + cam_zoom_x, cam_y + cam_zoom_y)
        self.icon_flag = False
        self.farm_flag = False
        for val, spr in enumerate(self.npc_sprites):
            if pygame.sprite.collide_rect(spr, khan):
                self.dialog_num = val
                self.icon_flag = True
            if pygame.sprite.collide_mask(spr, khan):
                self.mask(cam_x, cam_y, cam_zoom_x, cam_zoom_y)
                break
        else:
            for spr in self.house_sprites:
                if pygame.sprite.collide_mask(spr, khan):
                    self.mask(cam_x, cam_y, cam_zoom_x, cam_zoom_y)
                    break
            else:
                for val, spr in enumerate(self.forest_sprites):
                    if pygame.sprite.collide_rect(spr, khan):
                        self.farm_flag = True
                        self.farm_tree = val

        if self.icon_flag:
            self.one_icon.add(self.icons_sprite.sprites()[self.dialog_num])
            self.one_icon.draw(surface)
            self.one_icon.remove(self.icons_sprite.sprites()[self.dialog_num])
        if self.flag_action and self.icon_flag:
            self.ramka_sprite.draw(interface)
            dialog.draw_text(interface, self.dialog_num, dialog_part)
        if self.farm_flag and self.flag_action:
            spr = self.forest_farm_sprites.sprites()[self.farm_tree]
            self.cut_forest.add(spr)
            self.forest_farm_sprites.remove(self.forest_farm_sprites.sprites()[self.farm_tree])
            self.forest_sprites.remove(self.forest_sprites.sprites()[self.farm_tree])
            print(self.forest_sprites)
            print(self.forest_farm_sprites)
            print(self.cut_forest)

        self.stats_sprite.draw(interface)
        stats.draw_stats_text(interface, 0, 4, '4/20')
        stats.draw_stats_text(interface, 60, 4, '5/20')
        stats.draw_stats_text(interface, 120, 4, '20/20')

    def mask(self, cam_x, cam_y, cam_zoom_x, cam_zoom_y):
        self.cut_forest.update(-cam_x + cam_zoom_x, -cam_y + cam_zoom_y)
        self.forest_sprites.update(-cam_x + cam_zoom_x, -cam_y + cam_zoom_y)
        self.map_sprite.update(-cam_x + cam_zoom_x, -cam_y + cam_zoom_y)
        self.house_sprites.update(-cam_x + cam_zoom_x, -cam_y + cam_zoom_y)
        self.npc_sprites.update(-cam_x + cam_zoom_x, -cam_y + cam_zoom_y)
        self.icons_sprite.update(-cam_x + cam_zoom_x, -cam_y + cam_zoom_y)
        self.forest_farm_sprites.update(-cam_x + cam_zoom_x, -cam_y + cam_zoom_y)
