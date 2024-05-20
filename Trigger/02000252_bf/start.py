""" trigger/02000252_bf/start.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[151,152,153,154,155,156], visible=True)
        self.set_effect(trigger_ids=[601]) # 벨라 음성
        self.set_effect(trigger_ids=[602]) # 벨라 음성
        self.set_effect(trigger_ids=[603]) # 벨라 음성
        self.set_effect(trigger_ids=[8001])
        self.set_effect(trigger_ids=[8002])
        self.set_effect(trigger_ids=[8003])
        self.set_effect(trigger_ids=[8004])
        self.set_effect(trigger_ids=[8005])
        self.set_effect(trigger_ids=[8006])
        self.set_effect(trigger_ids=[8007])
        self.set_effect(trigger_ids=[8008])
        self.set_effect(trigger_ids=[8009])
        self.set_effect(trigger_ids=[8010])
        self.set_effect(trigger_ids=[8011])
        self.set_effect(trigger_ids=[8012])

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return 로딩딜레이(self.ctx)


class 로딩딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002521)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라소환(self.ctx)


class 연출해제(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_timer(timer_id='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라소환(self.ctx)


class 벨라소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera_path(path_ids=[8801,8802], return_view=False)
        self.spawn_monster(spawn_ids=[1001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 벨라대사(self.ctx)


class 벨라대사(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=벨라스킬딜레이, action='nextState')
        self.set_skip(state=벨라스킬딜레이)
        self.set_timer(timer_id='1', seconds=6)
        # self.set_effect(trigger_ids=[601], visible=True)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000252_BF__START__4$', time=3)
        # self.set_skip(state=벨라스킬딜레이)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사2(self.ctx)


class 벨라대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=8)
        # self.set_effect(trigger_ids=[602], visible=True)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000252_BF__START__5$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 벨라대사3(self.ctx)


class 벨라대사3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=4)
        self.set_scene_skip() # Missing State: State
        # self.set_effect(trigger_ids=[603], visible=True)
        self.set_dialogue(type=2, spawn_id=11000057, script='$02000252_BF__START__6$', time=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6243):
            return 벨라스킬딜레이(self.ctx)


class 벨라스킬딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=1001, patrol_name='MS2PatrolData_1')
        self.set_timer(timer_id='1', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1500):
            return 예고이펙트(self.ctx)


class 예고이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[8804])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(trigger_id=999, type='trigger', achieve='Bellafirst')
        self.set_effect(trigger_ids=[8001], visible=True)
        self.set_effect(trigger_ids=[8002], visible=True)
        self.set_effect(trigger_ids=[8003], visible=True)
        self.set_effect(trigger_ids=[8004], visible=True)
        self.set_effect(trigger_ids=[8005], visible=True)
        self.set_effect(trigger_ids=[8006], visible=True)
        self.set_effect(trigger_ids=[8007], visible=True)
        self.set_effect(trigger_ids=[8008], visible=True)
        self.set_effect(trigger_ids=[8009], visible=True)
        self.set_effect(trigger_ids=[8010], visible=True)
        self.set_effect(trigger_ids=[8011], visible=True)
        self.set_effect(trigger_ids=[8012], visible=True)
        self.set_timer(timer_id='2', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 스킬시작대기(self.ctx)


class 스킬시작대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entity_id=20002522, text_id=20002522)
        self.set_mesh(trigger_ids=[151,152,153,154,155,156])
        self.spawn_monster(spawn_ids=[1051], auto_target=False)
        self.spawn_monster(spawn_ids=[1052], auto_target=False)
        self.spawn_monster(spawn_ids=[1053], auto_target=False)
        self.spawn_monster(spawn_ids=[1054], auto_target=False)
        self.spawn_monster(spawn_ids=[1055], auto_target=False)
        self.spawn_monster(spawn_ids=[1056], auto_target=False)
        self.spawn_monster(spawn_ids=[1057], auto_target=False)
        self.spawn_monster(spawn_ids=[1058], auto_target=False)
        self.spawn_monster(spawn_ids=[1059], auto_target=False)
        self.spawn_monster(spawn_ids=[1060], auto_target=False)
        self.spawn_monster(spawn_ids=[1061], auto_target=False)
        self.spawn_monster(spawn_ids=[1062], auto_target=False)
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            self.destroy_monster(spawn_ids=[1001])
            return 스킬시작대기2(self.ctx)


class 스킬시작대기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=2)
        self.set_effect(trigger_ids=[8001])
        self.set_effect(trigger_ids=[8002])
        self.set_effect(trigger_ids=[8003])
        self.set_effect(trigger_ids=[8004])
        self.set_effect(trigger_ids=[8005])
        self.set_effect(trigger_ids=[8006])
        self.set_effect(trigger_ids=[8007])
        self.set_effect(trigger_ids=[8008])
        self.set_effect(trigger_ids=[8009])
        self.set_effect(trigger_ids=[8010])
        self.set_effect(trigger_ids=[8011])
        self.set_effect(trigger_ids=[8012])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 스킬To08(self.ctx)


class 스킬To08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[515], enable=True)
        self.set_skill(trigger_ids=[516], enable=True)
        self.set_skill(trigger_ids=[517], enable=True)
        self.set_skill(trigger_ids=[518], enable=True)
        self.set_skill(trigger_ids=[519], enable=True)
        self.set_skill(trigger_ids=[520], enable=True)
        self.set_skill(trigger_ids=[521], enable=True)
        self.set_skill(trigger_ids=[522], enable=True)
        self.set_skill(trigger_ids=[523], enable=True)
        self.set_skill(trigger_ids=[524], enable=True)
        self.set_skill(trigger_ids=[525], enable=True)
        self.set_skill(trigger_ids=[526], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬To07대기(self.ctx)


class 스킬To07대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[515])
        self.set_skill(trigger_ids=[516])
        self.set_skill(trigger_ids=[517])
        self.set_skill(trigger_ids=[518])
        self.set_skill(trigger_ids=[519])
        self.set_skill(trigger_ids=[520])
        self.set_skill(trigger_ids=[521])
        self.set_skill(trigger_ids=[522])
        self.set_skill(trigger_ids=[523])
        self.set_skill(trigger_ids=[524])
        self.set_skill(trigger_ids=[525])
        self.set_skill(trigger_ids=[526])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬To07(self.ctx)


class 스킬To07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[564], enable=True)
        self.set_skill(trigger_ids=[517], enable=True)
        self.set_skill(trigger_ids=[518], enable=True)
        self.set_skill(trigger_ids=[519], enable=True)
        self.set_skill(trigger_ids=[520], enable=True)
        self.set_skill(trigger_ids=[521], enable=True)
        self.set_skill(trigger_ids=[522], enable=True)
        self.set_skill(trigger_ids=[523], enable=True)
        self.set_skill(trigger_ids=[524], enable=True)
        self.set_skill(trigger_ids=[525], enable=True)
        self.set_skill(trigger_ids=[526], enable=True)
        self.set_skill(trigger_ids=[527], enable=True)
        self.set_skill(trigger_ids=[528], enable=True)
        self.set_skill(trigger_ids=[529], enable=True)
        self.set_skill(trigger_ids=[530], enable=True)
        self.set_skill(trigger_ids=[531], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬To06대기(self.ctx)


class 스킬To06대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[564])
        self.set_skill(trigger_ids=[517])
        self.set_skill(trigger_ids=[518])
        self.set_skill(trigger_ids=[519])
        self.set_skill(trigger_ids=[520])
        self.set_skill(trigger_ids=[521])
        self.set_skill(trigger_ids=[522])
        self.set_skill(trigger_ids=[523])
        self.set_skill(trigger_ids=[524])
        self.set_skill(trigger_ids=[525])
        self.set_skill(trigger_ids=[526])
        self.set_skill(trigger_ids=[527])
        self.set_skill(trigger_ids=[528])
        self.set_skill(trigger_ids=[529])
        self.set_skill(trigger_ids=[530])
        self.set_skill(trigger_ids=[531])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬To06(self.ctx)


class 스킬To06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[565], enable=True)
        self.set_skill(trigger_ids=[564], enable=True)
        self.set_skill(trigger_ids=[522], enable=True)
        self.set_skill(trigger_ids=[523], enable=True)
        self.set_skill(trigger_ids=[524], enable=True)
        self.set_skill(trigger_ids=[525], enable=True)
        self.set_skill(trigger_ids=[526], enable=True)
        self.set_skill(trigger_ids=[527], enable=True)
        self.set_skill(trigger_ids=[528], enable=True)
        self.set_skill(trigger_ids=[529], enable=True)
        self.set_skill(trigger_ids=[530], enable=True)
        self.set_skill(trigger_ids=[531], enable=True)
        self.set_skill(trigger_ids=[532], enable=True)
        self.set_skill(trigger_ids=[533], enable=True)
        self.set_skill(trigger_ids=[534], enable=True)
        self.set_skill(trigger_ids=[535], enable=True)
        self.set_skill(trigger_ids=[536], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬To05대기(self.ctx)


class 스킬To05대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=20002522)
        self.set_skill(trigger_ids=[565])
        self.set_skill(trigger_ids=[564])
        self.set_skill(trigger_ids=[522])
        self.set_skill(trigger_ids=[523])
        self.set_skill(trigger_ids=[524])
        self.set_skill(trigger_ids=[525])
        self.set_skill(trigger_ids=[526])
        self.set_skill(trigger_ids=[527])
        self.set_skill(trigger_ids=[528])
        self.set_skill(trigger_ids=[529])
        self.set_skill(trigger_ids=[530])
        self.set_skill(trigger_ids=[531])
        self.set_skill(trigger_ids=[532])
        self.set_skill(trigger_ids=[533])
        self.set_skill(trigger_ids=[534])
        self.set_skill(trigger_ids=[535])
        self.set_skill(trigger_ids=[536])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬To05(self.ctx)


class 스킬To05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[566], enable=True)
        self.set_skill(trigger_ids=[567], enable=True)
        self.set_skill(trigger_ids=[568], enable=True)
        self.set_skill(trigger_ids=[565], enable=True)
        self.set_skill(trigger_ids=[564], enable=True)
        self.set_skill(trigger_ids=[527], enable=True)
        self.set_skill(trigger_ids=[528], enable=True)
        self.set_skill(trigger_ids=[529], enable=True)
        self.set_skill(trigger_ids=[530], enable=True)
        self.set_skill(trigger_ids=[531], enable=True)
        self.set_skill(trigger_ids=[532], enable=True)
        self.set_skill(trigger_ids=[533], enable=True)
        self.set_skill(trigger_ids=[534], enable=True)
        self.set_skill(trigger_ids=[535], enable=True)
        self.set_skill(trigger_ids=[536], enable=True)
        self.set_skill(trigger_ids=[537], enable=True)
        self.set_skill(trigger_ids=[538], enable=True)
        self.set_skill(trigger_ids=[539], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬To04대기(self.ctx)


class 스킬To04대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[566])
        self.set_skill(trigger_ids=[567])
        self.set_skill(trigger_ids=[568])
        self.set_skill(trigger_ids=[565])
        self.set_skill(trigger_ids=[564])
        self.set_skill(trigger_ids=[527])
        self.set_skill(trigger_ids=[528])
        self.set_skill(trigger_ids=[529])
        self.set_skill(trigger_ids=[530])
        self.set_skill(trigger_ids=[531])
        self.set_skill(trigger_ids=[532])
        self.set_skill(trigger_ids=[533])
        self.set_skill(trigger_ids=[534])
        self.set_skill(trigger_ids=[535])
        self.set_skill(trigger_ids=[536])
        self.set_skill(trigger_ids=[537])
        self.set_skill(trigger_ids=[538])
        self.set_skill(trigger_ids=[539])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬To04(self.ctx)


class 스킬To04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[566])
        self.set_skill(trigger_ids=[567])
        self.set_skill(trigger_ids=[568])
        self.set_skill(trigger_ids=[565], enable=True)
        self.set_skill(trigger_ids=[532], enable=True)
        self.set_skill(trigger_ids=[533], enable=True)
        self.set_skill(trigger_ids=[534], enable=True)
        self.set_skill(trigger_ids=[535], enable=True)
        self.set_skill(trigger_ids=[536], enable=True)
        self.set_skill(trigger_ids=[537], enable=True)
        self.set_skill(trigger_ids=[538], enable=True)
        self.set_skill(trigger_ids=[539], enable=True)
        self.set_skill(trigger_ids=[540], enable=True)
        self.set_skill(trigger_ids=[541], enable=True)
        self.set_skill(trigger_ids=[542], enable=True)
        self.set_skill(trigger_ids=[543], enable=True)
        self.set_skill(trigger_ids=[544], enable=True)
        self.set_skill(trigger_ids=[545], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬To03대기(self.ctx)


class 스킬To03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[566])
        self.set_skill(trigger_ids=[567])
        self.set_skill(trigger_ids=[568])
        self.set_skill(trigger_ids=[565])
        self.set_skill(trigger_ids=[532])
        self.set_skill(trigger_ids=[533])
        self.set_skill(trigger_ids=[534])
        self.set_skill(trigger_ids=[535])
        self.set_skill(trigger_ids=[536])
        self.set_skill(trigger_ids=[537])
        self.set_skill(trigger_ids=[538])
        self.set_skill(trigger_ids=[539])
        self.set_skill(trigger_ids=[540])
        self.set_skill(trigger_ids=[541])
        self.set_skill(trigger_ids=[542])
        self.set_skill(trigger_ids=[543])
        self.set_skill(trigger_ids=[544])
        self.set_skill(trigger_ids=[545])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬To03(self.ctx)


class 스킬To03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[566], enable=True)
        self.set_skill(trigger_ids=[567], enable=True)
        self.set_skill(trigger_ids=[568], enable=True)
        self.set_skill(trigger_ids=[537], enable=True)
        self.set_skill(trigger_ids=[538], enable=True)
        self.set_skill(trigger_ids=[539], enable=True)
        self.set_skill(trigger_ids=[540], enable=True)
        self.set_skill(trigger_ids=[541], enable=True)
        self.set_skill(trigger_ids=[542], enable=True)
        self.set_skill(trigger_ids=[543], enable=True)
        self.set_skill(trigger_ids=[544], enable=True)
        self.set_skill(trigger_ids=[545], enable=True)
        self.set_skill(trigger_ids=[546], enable=True)
        self.set_skill(trigger_ids=[547], enable=True)
        self.set_skill(trigger_ids=[548], enable=True)
        self.set_skill(trigger_ids=[549], enable=True)
        self.set_skill(trigger_ids=[550], enable=True)
        self.set_skill(trigger_ids=[551], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬To02대기(self.ctx)


class 스킬To02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[566])
        self.set_skill(trigger_ids=[567])
        self.set_skill(trigger_ids=[568])
        self.set_skill(trigger_ids=[537])
        self.set_skill(trigger_ids=[538])
        self.set_skill(trigger_ids=[539])
        self.set_skill(trigger_ids=[540])
        self.set_skill(trigger_ids=[541])
        self.set_skill(trigger_ids=[542])
        self.set_skill(trigger_ids=[543])
        self.set_skill(trigger_ids=[544])
        self.set_skill(trigger_ids=[545])
        self.set_skill(trigger_ids=[546])
        self.set_skill(trigger_ids=[547])
        self.set_skill(trigger_ids=[548])
        self.set_skill(trigger_ids=[549])
        self.set_skill(trigger_ids=[550])
        self.set_skill(trigger_ids=[551])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬To02(self.ctx)


class 스킬To02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[540], enable=True)
        self.set_skill(trigger_ids=[541], enable=True)
        self.set_skill(trigger_ids=[542], enable=True)
        self.set_skill(trigger_ids=[543], enable=True)
        self.set_skill(trigger_ids=[544], enable=True)
        self.set_skill(trigger_ids=[545], enable=True)
        self.set_skill(trigger_ids=[546], enable=True)
        self.set_skill(trigger_ids=[547], enable=True)
        self.set_skill(trigger_ids=[548], enable=True)
        self.set_skill(trigger_ids=[549], enable=True)
        self.set_skill(trigger_ids=[550], enable=True)
        self.set_skill(trigger_ids=[551], enable=True)
        self.set_skill(trigger_ids=[552], enable=True)
        self.set_skill(trigger_ids=[553], enable=True)
        self.set_skill(trigger_ids=[554], enable=True)
        self.set_skill(trigger_ids=[555], enable=True)
        self.set_skill(trigger_ids=[556], enable=True)
        self.set_skill(trigger_ids=[557], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬To01대기(self.ctx)


class 스킬To01대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[540])
        self.set_skill(trigger_ids=[541])
        self.set_skill(trigger_ids=[542])
        self.set_skill(trigger_ids=[543])
        self.set_skill(trigger_ids=[544])
        self.set_skill(trigger_ids=[545])
        self.set_skill(trigger_ids=[546])
        self.set_skill(trigger_ids=[547])
        self.set_skill(trigger_ids=[548])
        self.set_skill(trigger_ids=[549])
        self.set_skill(trigger_ids=[550])
        self.set_skill(trigger_ids=[551])
        self.set_skill(trigger_ids=[552])
        self.set_skill(trigger_ids=[553])
        self.set_skill(trigger_ids=[554])
        self.set_skill(trigger_ids=[555])
        self.set_skill(trigger_ids=[556])
        self.set_skill(trigger_ids=[557])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬To01(self.ctx)


class 스킬To01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[546], enable=True)
        self.set_skill(trigger_ids=[547], enable=True)
        self.set_skill(trigger_ids=[548], enable=True)
        self.set_skill(trigger_ids=[549], enable=True)
        self.set_skill(trigger_ids=[550], enable=True)
        self.set_skill(trigger_ids=[551], enable=True)
        self.set_skill(trigger_ids=[552], enable=True)
        self.set_skill(trigger_ids=[553], enable=True)
        self.set_skill(trigger_ids=[554], enable=True)
        self.set_skill(trigger_ids=[555], enable=True)
        self.set_skill(trigger_ids=[556], enable=True)
        self.set_skill(trigger_ids=[557], enable=True)
        self.set_skill(trigger_ids=[558], enable=True)
        self.set_skill(trigger_ids=[559], enable=True)
        self.set_skill(trigger_ids=[560], enable=True)
        self.set_skill(trigger_ids=[561], enable=True)
        self.set_skill(trigger_ids=[562], enable=True)
        self.set_skill(trigger_ids=[563], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬00대기(self.ctx)


class 스킬00대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[546])
        self.set_skill(trigger_ids=[547])
        self.set_skill(trigger_ids=[548])
        self.set_skill(trigger_ids=[549])
        self.set_skill(trigger_ids=[550])
        self.set_skill(trigger_ids=[551])
        self.set_skill(trigger_ids=[552])
        self.set_skill(trigger_ids=[553])
        self.set_skill(trigger_ids=[554])
        self.set_skill(trigger_ids=[555])
        self.set_skill(trigger_ids=[556])
        self.set_skill(trigger_ids=[557])
        self.set_skill(trigger_ids=[558])
        self.set_skill(trigger_ids=[559])
        self.set_skill(trigger_ids=[560])
        self.set_skill(trigger_ids=[561])
        self.set_skill(trigger_ids=[562])
        self.set_skill(trigger_ids=[563])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬00(self.ctx)


class 스킬00(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[552], enable=True)
        self.set_skill(trigger_ids=[553], enable=True)
        self.set_skill(trigger_ids=[554], enable=True)
        self.set_skill(trigger_ids=[555], enable=True)
        self.set_skill(trigger_ids=[556], enable=True)
        self.set_skill(trigger_ids=[557], enable=True)
        self.set_skill(trigger_ids=[558], enable=True)
        self.set_skill(trigger_ids=[559], enable=True)
        self.set_skill(trigger_ids=[560], enable=True)
        self.set_skill(trigger_ids=[561], enable=True)
        self.set_skill(trigger_ids=[562], enable=True)
        self.set_skill(trigger_ids=[563], enable=True)
        self.set_skill(trigger_ids=[301], enable=True)
        self.set_skill(trigger_ids=[302], enable=True)
        self.set_skill(trigger_ids=[303], enable=True)
        self.set_skill(trigger_ids=[304], enable=True)
        self.set_skill(trigger_ids=[305], enable=True)
        self.set_skill(trigger_ids=[306], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬0_5대기(self.ctx)


class 스킬0_5대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[552])
        self.set_skill(trigger_ids=[553])
        self.set_skill(trigger_ids=[554])
        self.set_skill(trigger_ids=[555])
        self.set_skill(trigger_ids=[556])
        self.set_skill(trigger_ids=[557])
        self.set_skill(trigger_ids=[558])
        self.set_skill(trigger_ids=[559])
        self.set_skill(trigger_ids=[560])
        self.set_skill(trigger_ids=[561])
        self.set_skill(trigger_ids=[562])
        self.set_skill(trigger_ids=[563])
        self.set_skill(trigger_ids=[301])
        self.set_skill(trigger_ids=[302])
        self.set_skill(trigger_ids=[303])
        self.set_skill(trigger_ids=[304])
        self.set_skill(trigger_ids=[305])
        self.set_skill(trigger_ids=[306])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬0_5(self.ctx)


class 스킬0_5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[558], enable=True)
        self.set_skill(trigger_ids=[559], enable=True)
        self.set_skill(trigger_ids=[560], enable=True)
        self.set_skill(trigger_ids=[561], enable=True)
        self.set_skill(trigger_ids=[562], enable=True)
        self.set_skill(trigger_ids=[563], enable=True)
        self.set_skill(trigger_ids=[301], enable=True)
        self.set_skill(trigger_ids=[302], enable=True)
        self.set_skill(trigger_ids=[303], enable=True)
        self.set_skill(trigger_ids=[304], enable=True)
        self.set_skill(trigger_ids=[305], enable=True)
        self.set_skill(trigger_ids=[306], enable=True)
        self.set_skill(trigger_ids=[307], enable=True)
        self.set_skill(trigger_ids=[308], enable=True)
        self.set_skill(trigger_ids=[309], enable=True)
        self.set_skill(trigger_ids=[310], enable=True)
        self.set_skill(trigger_ids=[311], enable=True)
        self.set_skill(trigger_ids=[312], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬01대기(self.ctx)


class 스킬01대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[558])
        self.set_skill(trigger_ids=[559])
        self.set_skill(trigger_ids=[560])
        self.set_skill(trigger_ids=[561])
        self.set_skill(trigger_ids=[562])
        self.set_skill(trigger_ids=[563])
        self.set_skill(trigger_ids=[301])
        self.set_skill(trigger_ids=[302])
        self.set_skill(trigger_ids=[303])
        self.set_skill(trigger_ids=[304])
        self.set_skill(trigger_ids=[305])
        self.set_skill(trigger_ids=[306])
        self.set_skill(trigger_ids=[307])
        self.set_skill(trigger_ids=[308])
        self.set_skill(trigger_ids=[309])
        self.set_skill(trigger_ids=[310])
        self.set_skill(trigger_ids=[311])
        self.set_skill(trigger_ids=[312])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬01(self.ctx)


class 스킬01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[301], enable=True)
        self.set_skill(trigger_ids=[302], enable=True)
        self.set_skill(trigger_ids=[303], enable=True)
        self.set_skill(trigger_ids=[304], enable=True)
        self.set_skill(trigger_ids=[305], enable=True)
        self.set_skill(trigger_ids=[306], enable=True)
        self.set_skill(trigger_ids=[307], enable=True)
        self.set_skill(trigger_ids=[308], enable=True)
        self.set_skill(trigger_ids=[309], enable=True)
        self.set_skill(trigger_ids=[310], enable=True)
        self.set_skill(trigger_ids=[311], enable=True)
        self.set_skill(trigger_ids=[312], enable=True)
        self.set_skill(trigger_ids=[313], enable=True)
        self.set_skill(trigger_ids=[314], enable=True)
        self.set_skill(trigger_ids=[315], enable=True)
        self.set_skill(trigger_ids=[316], enable=True)
        self.set_skill(trigger_ids=[317], enable=True)
        self.set_skill(trigger_ids=[318], enable=True)
        self.set_skill(trigger_ids=[319], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬02대기(self.ctx)


class 스킬02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[301])
        self.set_skill(trigger_ids=[302])
        self.set_skill(trigger_ids=[303])
        self.set_skill(trigger_ids=[304])
        self.set_skill(trigger_ids=[305])
        self.set_skill(trigger_ids=[306])
        self.set_skill(trigger_ids=[307])
        self.set_skill(trigger_ids=[308])
        self.set_skill(trigger_ids=[309])
        self.set_skill(trigger_ids=[310])
        self.set_skill(trigger_ids=[311])
        self.set_skill(trigger_ids=[312])
        self.set_skill(trigger_ids=[313])
        self.set_skill(trigger_ids=[314])
        self.set_skill(trigger_ids=[315])
        self.set_skill(trigger_ids=[316])
        self.set_skill(trigger_ids=[317])
        self.set_skill(trigger_ids=[318])
        self.set_skill(trigger_ids=[319])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬02(self.ctx)


class 스킬02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[307], enable=True)
        self.set_skill(trigger_ids=[308], enable=True)
        self.set_skill(trigger_ids=[309], enable=True)
        self.set_skill(trigger_ids=[310], enable=True)
        self.set_skill(trigger_ids=[311], enable=True)
        self.set_skill(trigger_ids=[312], enable=True)
        self.set_skill(trigger_ids=[313], enable=True)
        self.set_skill(trigger_ids=[314], enable=True)
        self.set_skill(trigger_ids=[315], enable=True)
        self.set_skill(trigger_ids=[316], enable=True)
        self.set_skill(trigger_ids=[317], enable=True)
        self.set_skill(trigger_ids=[318], enable=True)
        self.set_skill(trigger_ids=[319], enable=True)
        self.set_skill(trigger_ids=[320], enable=True)
        self.set_skill(trigger_ids=[321], enable=True)
        self.set_skill(trigger_ids=[322], enable=True)
        self.set_skill(trigger_ids=[323], enable=True)
        self.set_skill(trigger_ids=[324], enable=True)
        self.set_skill(trigger_ids=[325], enable=True)
        self.set_skill(trigger_ids=[326], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬03대기(self.ctx)


class 스킬03대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[307])
        self.set_skill(trigger_ids=[308])
        self.set_skill(trigger_ids=[309])
        self.set_skill(trigger_ids=[310])
        self.set_skill(trigger_ids=[311])
        self.set_skill(trigger_ids=[312])
        self.set_skill(trigger_ids=[313])
        self.set_skill(trigger_ids=[314])
        self.set_skill(trigger_ids=[315])
        self.set_skill(trigger_ids=[316])
        self.set_skill(trigger_ids=[317])
        self.set_skill(trigger_ids=[318])
        self.set_skill(trigger_ids=[319])
        self.set_skill(trigger_ids=[320])
        self.set_skill(trigger_ids=[321])
        self.set_skill(trigger_ids=[322])
        self.set_skill(trigger_ids=[323])
        self.set_skill(trigger_ids=[324])
        self.set_skill(trigger_ids=[325])
        self.set_skill(trigger_ids=[326])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬03(self.ctx)


class 스킬03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[313], enable=True)
        self.set_skill(trigger_ids=[314], enable=True)
        self.set_skill(trigger_ids=[315], enable=True)
        self.set_skill(trigger_ids=[316], enable=True)
        self.set_skill(trigger_ids=[317], enable=True)
        self.set_skill(trigger_ids=[318], enable=True)
        self.set_skill(trigger_ids=[319], enable=True)
        self.set_skill(trigger_ids=[320], enable=True)
        self.set_skill(trigger_ids=[321], enable=True)
        self.set_skill(trigger_ids=[322], enable=True)
        self.set_skill(trigger_ids=[323], enable=True)
        self.set_skill(trigger_ids=[324], enable=True)
        self.set_skill(trigger_ids=[325], enable=True)
        self.set_skill(trigger_ids=[326], enable=True)
        self.set_skill(trigger_ids=[327], enable=True)
        self.set_skill(trigger_ids=[328], enable=True)
        self.set_skill(trigger_ids=[329], enable=True)
        self.set_skill(trigger_ids=[330], enable=True)
        self.set_skill(trigger_ids=[331], enable=True)
        self.set_skill(trigger_ids=[332], enable=True)
        self.set_skill(trigger_ids=[333], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬04대기(self.ctx)


class 스킬04대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[313])
        self.set_skill(trigger_ids=[314])
        self.set_skill(trigger_ids=[315])
        self.set_skill(trigger_ids=[316])
        self.set_skill(trigger_ids=[317])
        self.set_skill(trigger_ids=[318])
        self.set_skill(trigger_ids=[319])
        self.set_skill(trigger_ids=[320])
        self.set_skill(trigger_ids=[321])
        self.set_skill(trigger_ids=[322])
        self.set_skill(trigger_ids=[323])
        self.set_skill(trigger_ids=[324])
        self.set_skill(trigger_ids=[325])
        self.set_skill(trigger_ids=[326])
        self.set_skill(trigger_ids=[327])
        self.set_skill(trigger_ids=[328])
        self.set_skill(trigger_ids=[329])
        self.set_skill(trigger_ids=[330])
        self.set_skill(trigger_ids=[331])
        self.set_skill(trigger_ids=[332])
        self.set_skill(trigger_ids=[333])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬04(self.ctx)


class 스킬04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[320], enable=True)
        self.set_skill(trigger_ids=[321], enable=True)
        self.set_skill(trigger_ids=[322], enable=True)
        self.set_skill(trigger_ids=[323], enable=True)
        self.set_skill(trigger_ids=[324], enable=True)
        self.set_skill(trigger_ids=[325], enable=True)
        self.set_skill(trigger_ids=[326], enable=True)
        self.set_skill(trigger_ids=[327], enable=True)
        self.set_skill(trigger_ids=[328], enable=True)
        self.set_skill(trigger_ids=[329], enable=True)
        self.set_skill(trigger_ids=[330], enable=True)
        self.set_skill(trigger_ids=[331], enable=True)
        self.set_skill(trigger_ids=[332], enable=True)
        self.set_skill(trigger_ids=[333], enable=True)
        self.set_skill(trigger_ids=[334], enable=True)
        self.set_skill(trigger_ids=[335], enable=True)
        self.set_skill(trigger_ids=[336], enable=True)
        self.set_skill(trigger_ids=[337], enable=True)
        self.set_skill(trigger_ids=[338], enable=True)
        self.set_skill(trigger_ids=[339], enable=True)
        self.set_skill(trigger_ids=[340], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬05대기(self.ctx)


class 스킬05대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[320])
        self.set_skill(trigger_ids=[321])
        self.set_skill(trigger_ids=[322])
        self.set_skill(trigger_ids=[323])
        self.set_skill(trigger_ids=[324])
        self.set_skill(trigger_ids=[325])
        self.set_skill(trigger_ids=[326])
        self.set_skill(trigger_ids=[327])
        self.set_skill(trigger_ids=[328])
        self.set_skill(trigger_ids=[329])
        self.set_skill(trigger_ids=[330])
        self.set_skill(trigger_ids=[331])
        self.set_skill(trigger_ids=[332])
        self.set_skill(trigger_ids=[333])
        self.set_skill(trigger_ids=[334])
        self.set_skill(trigger_ids=[335])
        self.set_skill(trigger_ids=[336])
        self.set_skill(trigger_ids=[337])
        self.set_skill(trigger_ids=[338])
        self.set_skill(trigger_ids=[339])
        self.set_skill(trigger_ids=[340])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬05(self.ctx)


class 스킬05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[327], enable=True)
        self.set_skill(trigger_ids=[328], enable=True)
        self.set_skill(trigger_ids=[329], enable=True)
        self.set_skill(trigger_ids=[330], enable=True)
        self.set_skill(trigger_ids=[331], enable=True)
        self.set_skill(trigger_ids=[332], enable=True)
        self.set_skill(trigger_ids=[333], enable=True)
        self.set_skill(trigger_ids=[334], enable=True)
        self.set_skill(trigger_ids=[335], enable=True)
        self.set_skill(trigger_ids=[336], enable=True)
        self.set_skill(trigger_ids=[337], enable=True)
        self.set_skill(trigger_ids=[338], enable=True)
        self.set_skill(trigger_ids=[339], enable=True)
        self.set_skill(trigger_ids=[340], enable=True)
        self.set_skill(trigger_ids=[341], enable=True)
        self.set_skill(trigger_ids=[342], enable=True)
        self.set_skill(trigger_ids=[343], enable=True)
        self.set_skill(trigger_ids=[344], enable=True)
        self.set_skill(trigger_ids=[345], enable=True)
        self.set_skill(trigger_ids=[346], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬06대기(self.ctx)


class 스킬06대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[327])
        self.set_skill(trigger_ids=[328])
        self.set_skill(trigger_ids=[329])
        self.set_skill(trigger_ids=[330])
        self.set_skill(trigger_ids=[331])
        self.set_skill(trigger_ids=[332])
        self.set_skill(trigger_ids=[333])
        self.set_skill(trigger_ids=[334])
        self.set_skill(trigger_ids=[335])
        self.set_skill(trigger_ids=[336])
        self.set_skill(trigger_ids=[337])
        self.set_skill(trigger_ids=[338])
        self.set_skill(trigger_ids=[339])
        self.set_skill(trigger_ids=[340])
        self.set_skill(trigger_ids=[341])
        self.set_skill(trigger_ids=[342])
        self.set_skill(trigger_ids=[343])
        self.set_skill(trigger_ids=[344])
        self.set_skill(trigger_ids=[345])
        self.set_skill(trigger_ids=[346])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬06(self.ctx)


class 스킬06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[334], enable=True)
        self.set_skill(trigger_ids=[335], enable=True)
        self.set_skill(trigger_ids=[336], enable=True)
        self.set_skill(trigger_ids=[337], enable=True)
        self.set_skill(trigger_ids=[338], enable=True)
        self.set_skill(trigger_ids=[339], enable=True)
        self.set_skill(trigger_ids=[340], enable=True)
        self.set_skill(trigger_ids=[341], enable=True)
        self.set_skill(trigger_ids=[342], enable=True)
        self.set_skill(trigger_ids=[343], enable=True)
        self.set_skill(trigger_ids=[344], enable=True)
        self.set_skill(trigger_ids=[345], enable=True)
        self.set_skill(trigger_ids=[346], enable=True)
        self.set_skill(trigger_ids=[347], enable=True)
        self.set_skill(trigger_ids=[348], enable=True)
        self.set_skill(trigger_ids=[349], enable=True)
        self.set_skill(trigger_ids=[350], enable=True)
        self.set_skill(trigger_ids=[351], enable=True)
        self.set_skill(trigger_ids=[352], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬07대기(self.ctx)


class 스킬07대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[334])
        self.set_skill(trigger_ids=[335])
        self.set_skill(trigger_ids=[336])
        self.set_skill(trigger_ids=[337])
        self.set_skill(trigger_ids=[338])
        self.set_skill(trigger_ids=[339])
        self.set_skill(trigger_ids=[340])
        self.set_skill(trigger_ids=[341])
        self.set_skill(trigger_ids=[342])
        self.set_skill(trigger_ids=[343])
        self.set_skill(trigger_ids=[344])
        self.set_skill(trigger_ids=[345])
        self.set_skill(trigger_ids=[346])
        self.set_skill(trigger_ids=[347])
        self.set_skill(trigger_ids=[348])
        self.set_skill(trigger_ids=[349])
        self.set_skill(trigger_ids=[350])
        self.set_skill(trigger_ids=[351])
        self.set_skill(trigger_ids=[352])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬07(self.ctx)


class 스킬07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[341], enable=True)
        self.set_skill(trigger_ids=[342], enable=True)
        self.set_skill(trigger_ids=[343], enable=True)
        self.set_skill(trigger_ids=[344], enable=True)
        self.set_skill(trigger_ids=[345], enable=True)
        self.set_skill(trigger_ids=[346], enable=True)
        self.set_skill(trigger_ids=[347], enable=True)
        self.set_skill(trigger_ids=[348], enable=True)
        self.set_skill(trigger_ids=[349], enable=True)
        self.set_skill(trigger_ids=[350], enable=True)
        self.set_skill(trigger_ids=[351], enable=True)
        self.set_skill(trigger_ids=[352], enable=True)
        self.set_skill(trigger_ids=[353], enable=True)
        self.set_skill(trigger_ids=[354], enable=True)
        self.set_skill(trigger_ids=[355], enable=True)
        self.set_skill(trigger_ids=[356], enable=True)
        self.set_skill(trigger_ids=[357], enable=True)
        self.set_skill(trigger_ids=[358], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬08대기(self.ctx)


class 스킬08대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[341])
        self.set_skill(trigger_ids=[342])
        self.set_skill(trigger_ids=[343])
        self.set_skill(trigger_ids=[344])
        self.set_skill(trigger_ids=[345])
        self.set_skill(trigger_ids=[346])
        self.set_skill(trigger_ids=[347])
        self.set_skill(trigger_ids=[348])
        self.set_skill(trigger_ids=[349])
        self.set_skill(trigger_ids=[350])
        self.set_skill(trigger_ids=[351])
        self.set_skill(trigger_ids=[352])
        self.set_skill(trigger_ids=[353])
        self.set_skill(trigger_ids=[354])
        self.set_skill(trigger_ids=[355])
        self.set_skill(trigger_ids=[356])
        self.set_skill(trigger_ids=[357])
        self.set_skill(trigger_ids=[358])

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000409], state=0):
            return 굳음(self.ctx)
        return 스킬08(self.ctx)


class 굳음(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=20)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 스킬08(self.ctx)


class 스킬08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[1101,1102,1103,1104,1105,1106,1107,1108], interval=100)
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[347], enable=True)
        self.set_skill(trigger_ids=[348], enable=True)
        self.set_skill(trigger_ids=[349], enable=True)
        self.set_skill(trigger_ids=[350], enable=True)
        self.set_skill(trigger_ids=[351], enable=True)
        self.set_skill(trigger_ids=[352], enable=True)
        self.set_skill(trigger_ids=[353], enable=True)
        self.set_skill(trigger_ids=[354], enable=True)
        self.set_skill(trigger_ids=[355], enable=True)
        self.set_skill(trigger_ids=[356], enable=True)
        self.set_skill(trigger_ids=[357], enable=True)
        self.set_skill(trigger_ids=[358], enable=True)
        self.set_skill(trigger_ids=[359], enable=True)
        self.set_skill(trigger_ids=[360], enable=True)
        self.set_skill(trigger_ids=[361], enable=True)
        self.set_skill(trigger_ids=[362], enable=True)
        self.set_skill(trigger_ids=[363], enable=True)
        self.set_skill(trigger_ids=[364], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬09대기(self.ctx)


class 스킬09대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[347])
        self.set_skill(trigger_ids=[348])
        self.set_skill(trigger_ids=[349])
        self.set_skill(trigger_ids=[350])
        self.set_skill(trigger_ids=[351])
        self.set_skill(trigger_ids=[352])
        self.set_skill(trigger_ids=[353])
        self.set_skill(trigger_ids=[354])
        self.set_skill(trigger_ids=[355])
        self.set_skill(trigger_ids=[356])
        self.set_skill(trigger_ids=[357])
        self.set_skill(trigger_ids=[358])
        self.set_skill(trigger_ids=[359])
        self.set_skill(trigger_ids=[360])
        self.set_skill(trigger_ids=[361])
        self.set_skill(trigger_ids=[362])
        self.set_skill(trigger_ids=[363])
        self.set_skill(trigger_ids=[364])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬09(self.ctx)


class 스킬09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[353], enable=True)
        self.set_skill(trigger_ids=[354], enable=True)
        self.set_skill(trigger_ids=[355], enable=True)
        self.set_skill(trigger_ids=[356], enable=True)
        self.set_skill(trigger_ids=[357], enable=True)
        self.set_skill(trigger_ids=[358], enable=True)
        self.set_skill(trigger_ids=[359], enable=True)
        self.set_skill(trigger_ids=[360], enable=True)
        self.set_skill(trigger_ids=[361], enable=True)
        self.set_skill(trigger_ids=[362], enable=True)
        self.set_skill(trigger_ids=[363], enable=True)
        self.set_skill(trigger_ids=[364], enable=True)
        self.set_skill(trigger_ids=[365], enable=True)
        self.set_skill(trigger_ids=[366], enable=True)
        self.set_skill(trigger_ids=[367], enable=True)
        self.set_skill(trigger_ids=[368], enable=True)
        self.set_skill(trigger_ids=[369], enable=True)
        self.set_skill(trigger_ids=[370], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬10대기(self.ctx)


class 스킬10대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[353])
        self.set_skill(trigger_ids=[354])
        self.set_skill(trigger_ids=[355])
        self.set_skill(trigger_ids=[356])
        self.set_skill(trigger_ids=[357])
        self.set_skill(trigger_ids=[358])
        self.set_skill(trigger_ids=[359])
        self.set_skill(trigger_ids=[360])
        self.set_skill(trigger_ids=[361])
        self.set_skill(trigger_ids=[362])
        self.set_skill(trigger_ids=[363])
        self.set_skill(trigger_ids=[364])
        self.set_skill(trigger_ids=[365])
        self.set_skill(trigger_ids=[366])
        self.set_skill(trigger_ids=[367])
        self.set_skill(trigger_ids=[368])
        self.set_skill(trigger_ids=[369])
        self.set_skill(trigger_ids=[370])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬10(self.ctx)


class 스킬10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[359], enable=True)
        self.set_skill(trigger_ids=[360], enable=True)
        self.set_skill(trigger_ids=[361], enable=True)
        self.set_skill(trigger_ids=[362], enable=True)
        self.set_skill(trigger_ids=[363], enable=True)
        self.set_skill(trigger_ids=[364], enable=True)
        self.set_skill(trigger_ids=[365], enable=True)
        self.set_skill(trigger_ids=[366], enable=True)
        self.set_skill(trigger_ids=[367], enable=True)
        self.set_skill(trigger_ids=[368], enable=True)
        self.set_skill(trigger_ids=[369], enable=True)
        self.set_skill(trigger_ids=[370], enable=True)
        self.set_skill(trigger_ids=[371], enable=True)
        self.set_skill(trigger_ids=[372], enable=True)
        self.set_skill(trigger_ids=[373], enable=True)
        self.set_skill(trigger_ids=[374], enable=True)
        self.set_skill(trigger_ids=[375], enable=True)
        self.set_skill(trigger_ids=[376], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬11대기(self.ctx)


class 스킬11대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1')
        self.set_skill(trigger_ids=[359])
        self.set_skill(trigger_ids=[360])
        self.set_skill(trigger_ids=[361])
        self.set_skill(trigger_ids=[362])
        self.set_skill(trigger_ids=[363])
        self.set_skill(trigger_ids=[364])
        self.set_skill(trigger_ids=[365])
        self.set_skill(trigger_ids=[366])
        self.set_skill(trigger_ids=[367])
        self.set_skill(trigger_ids=[368])
        self.set_skill(trigger_ids=[369])
        self.set_skill(trigger_ids=[370])
        self.set_skill(trigger_ids=[371])
        self.set_skill(trigger_ids=[372])
        self.set_skill(trigger_ids=[373])
        self.set_skill(trigger_ids=[374])
        self.set_skill(trigger_ids=[375])
        self.set_skill(trigger_ids=[376])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬12(self.ctx)


class 스킬12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[365], enable=True)
        self.set_skill(trigger_ids=[366], enable=True)
        self.set_skill(trigger_ids=[367], enable=True)
        self.set_skill(trigger_ids=[368], enable=True)
        self.set_skill(trigger_ids=[369], enable=True)
        self.set_skill(trigger_ids=[370], enable=True)
        self.set_skill(trigger_ids=[371], enable=True)
        self.set_skill(trigger_ids=[372], enable=True)
        self.set_skill(trigger_ids=[373], enable=True)
        self.set_skill(trigger_ids=[374], enable=True)
        self.set_skill(trigger_ids=[375], enable=True)
        self.set_skill(trigger_ids=[376], enable=True)
        self.set_skill(trigger_ids=[377], enable=True)
        self.set_skill(trigger_ids=[378], enable=True)
        self.set_skill(trigger_ids=[379], enable=True)
        self.set_skill(trigger_ids=[380], enable=True)
        self.set_skill(trigger_ids=[381], enable=True)
        self.set_skill(trigger_ids=[382], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬13대기(self.ctx)


class 스킬13대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[365])
        self.set_skill(trigger_ids=[366])
        self.set_skill(trigger_ids=[367])
        self.set_skill(trigger_ids=[368])
        self.set_skill(trigger_ids=[369])
        self.set_skill(trigger_ids=[370])
        self.set_skill(trigger_ids=[371])
        self.set_skill(trigger_ids=[372])
        self.set_skill(trigger_ids=[373])
        self.set_skill(trigger_ids=[374])
        self.set_skill(trigger_ids=[375])
        self.set_skill(trigger_ids=[376])
        self.set_skill(trigger_ids=[377])
        self.set_skill(trigger_ids=[378])
        self.set_skill(trigger_ids=[379])
        self.set_skill(trigger_ids=[380])
        self.set_skill(trigger_ids=[381])
        self.set_skill(trigger_ids=[382])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬13(self.ctx)


class 스킬13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[371], enable=True)
        self.set_skill(trigger_ids=[372], enable=True)
        self.set_skill(trigger_ids=[373], enable=True)
        self.set_skill(trigger_ids=[374], enable=True)
        self.set_skill(trigger_ids=[375], enable=True)
        self.set_skill(trigger_ids=[376], enable=True)
        self.set_skill(trigger_ids=[377], enable=True)
        self.set_skill(trigger_ids=[378], enable=True)
        self.set_skill(trigger_ids=[379], enable=True)
        self.set_skill(trigger_ids=[380], enable=True)
        self.set_skill(trigger_ids=[381], enable=True)
        self.set_skill(trigger_ids=[382], enable=True)
        self.set_skill(trigger_ids=[383], enable=True)
        self.set_skill(trigger_ids=[384], enable=True)
        self.set_skill(trigger_ids=[385], enable=True)
        self.set_skill(trigger_ids=[386], enable=True)
        self.set_skill(trigger_ids=[387], enable=True)
        self.set_skill(trigger_ids=[388], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬14대기(self.ctx)


class 스킬14대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[371])
        self.set_skill(trigger_ids=[372])
        self.set_skill(trigger_ids=[373])
        self.set_skill(trigger_ids=[374])
        self.set_skill(trigger_ids=[375])
        self.set_skill(trigger_ids=[376])
        self.set_skill(trigger_ids=[377])
        self.set_skill(trigger_ids=[378])
        self.set_skill(trigger_ids=[379])
        self.set_skill(trigger_ids=[380])
        self.set_skill(trigger_ids=[381])
        self.set_skill(trigger_ids=[382])
        self.set_skill(trigger_ids=[383])
        self.set_skill(trigger_ids=[384])
        self.set_skill(trigger_ids=[385])
        self.set_skill(trigger_ids=[386])
        self.set_skill(trigger_ids=[387])
        self.set_skill(trigger_ids=[388])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬14(self.ctx)


class 스킬14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[377], enable=True)
        self.set_skill(trigger_ids=[378], enable=True)
        self.set_skill(trigger_ids=[379], enable=True)
        self.set_skill(trigger_ids=[380], enable=True)
        self.set_skill(trigger_ids=[381], enable=True)
        self.set_skill(trigger_ids=[382], enable=True)
        self.set_skill(trigger_ids=[383], enable=True)
        self.set_skill(trigger_ids=[384], enable=True)
        self.set_skill(trigger_ids=[385], enable=True)
        self.set_skill(trigger_ids=[386], enable=True)
        self.set_skill(trigger_ids=[387], enable=True)
        self.set_skill(trigger_ids=[388], enable=True)
        self.set_skill(trigger_ids=[389], enable=True)
        self.set_skill(trigger_ids=[390], enable=True)
        self.set_skill(trigger_ids=[391], enable=True)
        self.set_skill(trigger_ids=[392], enable=True)
        self.set_skill(trigger_ids=[393], enable=True)
        self.set_skill(trigger_ids=[394], enable=True)
        self.set_skill(trigger_ids=[395], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬15대기(self.ctx)


class 스킬15대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[377])
        self.set_skill(trigger_ids=[378])
        self.set_skill(trigger_ids=[379])
        self.set_skill(trigger_ids=[380])
        self.set_skill(trigger_ids=[381])
        self.set_skill(trigger_ids=[382])
        self.set_skill(trigger_ids=[383])
        self.set_skill(trigger_ids=[384])
        self.set_skill(trigger_ids=[385])
        self.set_skill(trigger_ids=[386])
        self.set_skill(trigger_ids=[387])
        self.set_skill(trigger_ids=[388])
        self.set_skill(trigger_ids=[389])
        self.set_skill(trigger_ids=[390])
        self.set_skill(trigger_ids=[391])
        self.set_skill(trigger_ids=[392])
        self.set_skill(trigger_ids=[393])
        self.set_skill(trigger_ids=[394])
        self.set_skill(trigger_ids=[395])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬15(self.ctx)


class 스킬15(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[383], enable=True)
        self.set_skill(trigger_ids=[384], enable=True)
        self.set_skill(trigger_ids=[385], enable=True)
        self.set_skill(trigger_ids=[386], enable=True)
        self.set_skill(trigger_ids=[387], enable=True)
        self.set_skill(trigger_ids=[388], enable=True)
        self.set_skill(trigger_ids=[389], enable=True)
        self.set_skill(trigger_ids=[390], enable=True)
        self.set_skill(trigger_ids=[391], enable=True)
        self.set_skill(trigger_ids=[392], enable=True)
        self.set_skill(trigger_ids=[393], enable=True)
        self.set_skill(trigger_ids=[394], enable=True)
        self.set_skill(trigger_ids=[395], enable=True)
        self.set_skill(trigger_ids=[396], enable=True)
        self.set_skill(trigger_ids=[397], enable=True)
        self.set_skill(trigger_ids=[398], enable=True)
        self.set_skill(trigger_ids=[399], enable=True)
        self.set_skill(trigger_ids=[400], enable=True)
        self.set_skill(trigger_ids=[401], enable=True)
        self.set_skill(trigger_ids=[402], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬16대기(self.ctx)


class 스킬16대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[383])
        self.set_skill(trigger_ids=[384])
        self.set_skill(trigger_ids=[385])
        self.set_skill(trigger_ids=[386])
        self.set_skill(trigger_ids=[387])
        self.set_skill(trigger_ids=[388])
        self.set_skill(trigger_ids=[389])
        self.set_skill(trigger_ids=[390])
        self.set_skill(trigger_ids=[391])
        self.set_skill(trigger_ids=[392])
        self.set_skill(trigger_ids=[393])
        self.set_skill(trigger_ids=[394])
        self.set_skill(trigger_ids=[395])
        self.set_skill(trigger_ids=[396])
        self.set_skill(trigger_ids=[397])
        self.set_skill(trigger_ids=[398])
        self.set_skill(trigger_ids=[399])
        self.set_skill(trigger_ids=[400])
        self.set_skill(trigger_ids=[401])
        self.set_skill(trigger_ids=[402])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬16(self.ctx)


class 스킬16(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[389], enable=True)
        self.set_skill(trigger_ids=[390], enable=True)
        self.set_skill(trigger_ids=[391], enable=True)
        self.set_skill(trigger_ids=[392], enable=True)
        self.set_skill(trigger_ids=[393], enable=True)
        self.set_skill(trigger_ids=[394], enable=True)
        self.set_skill(trigger_ids=[395], enable=True)
        self.set_skill(trigger_ids=[396], enable=True)
        self.set_skill(trigger_ids=[397], enable=True)
        self.set_skill(trigger_ids=[398], enable=True)
        self.set_skill(trigger_ids=[399], enable=True)
        self.set_skill(trigger_ids=[400], enable=True)
        self.set_skill(trigger_ids=[401], enable=True)
        self.set_skill(trigger_ids=[402], enable=True)
        self.set_skill(trigger_ids=[403], enable=True)
        self.set_skill(trigger_ids=[404], enable=True)
        self.set_skill(trigger_ids=[405], enable=True)
        self.set_skill(trigger_ids=[406], enable=True)
        self.set_skill(trigger_ids=[407], enable=True)
        self.set_skill(trigger_ids=[408], enable=True)
        self.set_skill(trigger_ids=[409], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬17대기(self.ctx)


class 스킬17대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[389])
        self.set_skill(trigger_ids=[390])
        self.set_skill(trigger_ids=[391])
        self.set_skill(trigger_ids=[392])
        self.set_skill(trigger_ids=[393])
        self.set_skill(trigger_ids=[394])
        self.set_skill(trigger_ids=[395])
        self.set_skill(trigger_ids=[396])
        self.set_skill(trigger_ids=[397])
        self.set_skill(trigger_ids=[398])
        self.set_skill(trigger_ids=[399])
        self.set_skill(trigger_ids=[400])
        self.set_skill(trigger_ids=[401])
        self.set_skill(trigger_ids=[402])
        self.set_skill(trigger_ids=[403])
        self.set_skill(trigger_ids=[404])
        self.set_skill(trigger_ids=[405])
        self.set_skill(trigger_ids=[406])
        self.set_skill(trigger_ids=[407])
        self.set_skill(trigger_ids=[408])
        self.set_skill(trigger_ids=[409])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬17(self.ctx)


class 스킬17(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[396], enable=True)
        self.set_skill(trigger_ids=[397], enable=True)
        self.set_skill(trigger_ids=[398], enable=True)
        self.set_skill(trigger_ids=[399], enable=True)
        self.set_skill(trigger_ids=[400], enable=True)
        self.set_skill(trigger_ids=[401], enable=True)
        self.set_skill(trigger_ids=[402], enable=True)
        self.set_skill(trigger_ids=[403], enable=True)
        self.set_skill(trigger_ids=[404], enable=True)
        self.set_skill(trigger_ids=[405], enable=True)
        self.set_skill(trigger_ids=[406], enable=True)
        self.set_skill(trigger_ids=[407], enable=True)
        self.set_skill(trigger_ids=[408], enable=True)
        self.set_skill(trigger_ids=[409], enable=True)
        self.set_skill(trigger_ids=[410], enable=True)
        self.set_skill(trigger_ids=[411], enable=True)
        self.set_skill(trigger_ids=[412], enable=True)
        self.set_skill(trigger_ids=[413], enable=True)
        self.set_skill(trigger_ids=[414], enable=True)
        self.set_skill(trigger_ids=[415], enable=True)
        self.set_skill(trigger_ids=[416], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬18대기(self.ctx)


class 스킬18대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[396])
        self.set_skill(trigger_ids=[397])
        self.set_skill(trigger_ids=[398])
        self.set_skill(trigger_ids=[399])
        self.set_skill(trigger_ids=[400])
        self.set_skill(trigger_ids=[401])
        self.set_skill(trigger_ids=[402])
        self.set_skill(trigger_ids=[403])
        self.set_skill(trigger_ids=[404])
        self.set_skill(trigger_ids=[405])
        self.set_skill(trigger_ids=[406])
        self.set_skill(trigger_ids=[407])
        self.set_skill(trigger_ids=[408])
        self.set_skill(trigger_ids=[409])
        self.set_skill(trigger_ids=[410])
        self.set_skill(trigger_ids=[411])
        self.set_skill(trigger_ids=[412])
        self.set_skill(trigger_ids=[413])
        self.set_skill(trigger_ids=[414])
        self.set_skill(trigger_ids=[415])
        self.set_skill(trigger_ids=[416])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬18(self.ctx)


class 스킬18(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[403], enable=True)
        self.set_skill(trigger_ids=[404], enable=True)
        self.set_skill(trigger_ids=[405], enable=True)
        self.set_skill(trigger_ids=[406], enable=True)
        self.set_skill(trigger_ids=[407], enable=True)
        self.set_skill(trigger_ids=[408], enable=True)
        self.set_skill(trigger_ids=[409], enable=True)
        self.set_skill(trigger_ids=[410], enable=True)
        self.set_skill(trigger_ids=[411], enable=True)
        self.set_skill(trigger_ids=[412], enable=True)
        self.set_skill(trigger_ids=[413], enable=True)
        self.set_skill(trigger_ids=[414], enable=True)
        self.set_skill(trigger_ids=[415], enable=True)
        self.set_skill(trigger_ids=[416], enable=True)
        self.set_skill(trigger_ids=[417], enable=True)
        self.set_skill(trigger_ids=[418], enable=True)
        self.set_skill(trigger_ids=[419], enable=True)
        self.set_skill(trigger_ids=[420], enable=True)
        self.set_skill(trigger_ids=[421], enable=True)
        self.set_skill(trigger_ids=[422], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬19대기(self.ctx)


class 스킬19대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[403])
        self.set_skill(trigger_ids=[404])
        self.set_skill(trigger_ids=[405])
        self.set_skill(trigger_ids=[406])
        self.set_skill(trigger_ids=[407])
        self.set_skill(trigger_ids=[408])
        self.set_skill(trigger_ids=[409])
        self.set_skill(trigger_ids=[410])
        self.set_skill(trigger_ids=[411])
        self.set_skill(trigger_ids=[412])
        self.set_skill(trigger_ids=[413])
        self.set_skill(trigger_ids=[414])
        self.set_skill(trigger_ids=[415])
        self.set_skill(trigger_ids=[416])
        self.set_skill(trigger_ids=[417])
        self.set_skill(trigger_ids=[418])
        self.set_skill(trigger_ids=[419])
        self.set_skill(trigger_ids=[420])
        self.set_skill(trigger_ids=[421])
        self.set_skill(trigger_ids=[422])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬19(self.ctx)


class 스킬19(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[410], enable=True)
        self.set_skill(trigger_ids=[411], enable=True)
        self.set_skill(trigger_ids=[412], enable=True)
        self.set_skill(trigger_ids=[413], enable=True)
        self.set_skill(trigger_ids=[414], enable=True)
        self.set_skill(trigger_ids=[415], enable=True)
        self.set_skill(trigger_ids=[416], enable=True)
        self.set_skill(trigger_ids=[417], enable=True)
        self.set_skill(trigger_ids=[418], enable=True)
        self.set_skill(trigger_ids=[419], enable=True)
        self.set_skill(trigger_ids=[420], enable=True)
        self.set_skill(trigger_ids=[421], enable=True)
        self.set_skill(trigger_ids=[422], enable=True)
        self.set_skill(trigger_ids=[423], enable=True)
        self.set_skill(trigger_ids=[424], enable=True)
        self.set_skill(trigger_ids=[425], enable=True)
        self.set_skill(trigger_ids=[426], enable=True)
        self.set_skill(trigger_ids=[427], enable=True)
        self.set_skill(trigger_ids=[428], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬20대기(self.ctx)


class 스킬20대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[410])
        self.set_skill(trigger_ids=[411])
        self.set_skill(trigger_ids=[412])
        self.set_skill(trigger_ids=[413])
        self.set_skill(trigger_ids=[414])
        self.set_skill(trigger_ids=[415])
        self.set_skill(trigger_ids=[416])
        self.set_skill(trigger_ids=[417])
        self.set_skill(trigger_ids=[418])
        self.set_skill(trigger_ids=[419])
        self.set_skill(trigger_ids=[420])
        self.set_skill(trigger_ids=[421])
        self.set_skill(trigger_ids=[422])
        self.set_skill(trigger_ids=[423])
        self.set_skill(trigger_ids=[424])
        self.set_skill(trigger_ids=[425])
        self.set_skill(trigger_ids=[426])
        self.set_skill(trigger_ids=[427])
        self.set_skill(trigger_ids=[428])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬20(self.ctx)


class 스킬20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[417], enable=True)
        self.set_skill(trigger_ids=[418], enable=True)
        self.set_skill(trigger_ids=[419], enable=True)
        self.set_skill(trigger_ids=[420], enable=True)
        self.set_skill(trigger_ids=[421], enable=True)
        self.set_skill(trigger_ids=[422], enable=True)
        self.set_skill(trigger_ids=[423], enable=True)
        self.set_skill(trigger_ids=[424], enable=True)
        self.set_skill(trigger_ids=[425], enable=True)
        self.set_skill(trigger_ids=[426], enable=True)
        self.set_skill(trigger_ids=[427], enable=True)
        self.set_skill(trigger_ids=[428], enable=True)
        self.set_skill(trigger_ids=[429], enable=True)
        self.set_skill(trigger_ids=[430], enable=True)
        self.set_skill(trigger_ids=[431], enable=True)
        self.set_skill(trigger_ids=[432], enable=True)
        self.set_skill(trigger_ids=[433], enable=True)
        self.set_skill(trigger_ids=[434], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬21대기(self.ctx)


class 스킬21대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[417])
        self.set_skill(trigger_ids=[418])
        self.set_skill(trigger_ids=[419])
        self.set_skill(trigger_ids=[420])
        self.set_skill(trigger_ids=[421])
        self.set_skill(trigger_ids=[422])
        self.set_skill(trigger_ids=[423])
        self.set_skill(trigger_ids=[424])
        self.set_skill(trigger_ids=[425])
        self.set_skill(trigger_ids=[426])
        self.set_skill(trigger_ids=[427])
        self.set_skill(trigger_ids=[428])
        self.set_skill(trigger_ids=[429])
        self.set_skill(trigger_ids=[430])
        self.set_skill(trigger_ids=[431])
        self.set_skill(trigger_ids=[432])
        self.set_skill(trigger_ids=[433])
        self.set_skill(trigger_ids=[434])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬21(self.ctx)


class 스킬21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[423], enable=True)
        self.set_skill(trigger_ids=[424], enable=True)
        self.set_skill(trigger_ids=[425], enable=True)
        self.set_skill(trigger_ids=[426], enable=True)
        self.set_skill(trigger_ids=[427], enable=True)
        self.set_skill(trigger_ids=[428], enable=True)
        self.set_skill(trigger_ids=[429], enable=True)
        self.set_skill(trigger_ids=[430], enable=True)
        self.set_skill(trigger_ids=[431], enable=True)
        self.set_skill(trigger_ids=[432], enable=True)
        self.set_skill(trigger_ids=[433], enable=True)
        self.set_skill(trigger_ids=[434], enable=True)
        self.set_skill(trigger_ids=[435], enable=True)
        self.set_skill(trigger_ids=[436], enable=True)
        self.set_skill(trigger_ids=[437], enable=True)
        self.set_skill(trigger_ids=[438], enable=True)
        self.set_skill(trigger_ids=[439], enable=True)
        self.set_skill(trigger_ids=[440], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬22대기(self.ctx)


class 스킬22대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[423])
        self.set_skill(trigger_ids=[424])
        self.set_skill(trigger_ids=[425])
        self.set_skill(trigger_ids=[426])
        self.set_skill(trigger_ids=[427])
        self.set_skill(trigger_ids=[428])
        self.set_skill(trigger_ids=[429])
        self.set_skill(trigger_ids=[430])
        self.set_skill(trigger_ids=[431])
        self.set_skill(trigger_ids=[432])
        self.set_skill(trigger_ids=[433])
        self.set_skill(trigger_ids=[434])
        self.set_skill(trigger_ids=[435])
        self.set_skill(trigger_ids=[436])
        self.set_skill(trigger_ids=[437])
        self.set_skill(trigger_ids=[438])
        self.set_skill(trigger_ids=[439])
        self.set_skill(trigger_ids=[440])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬22(self.ctx)


class 스킬22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[429], enable=True)
        self.set_skill(trigger_ids=[430], enable=True)
        self.set_skill(trigger_ids=[431], enable=True)
        self.set_skill(trigger_ids=[432], enable=True)
        self.set_skill(trigger_ids=[433], enable=True)
        self.set_skill(trigger_ids=[434], enable=True)
        self.set_skill(trigger_ids=[435], enable=True)
        self.set_skill(trigger_ids=[436], enable=True)
        self.set_skill(trigger_ids=[437], enable=True)
        self.set_skill(trigger_ids=[438], enable=True)
        self.set_skill(trigger_ids=[439], enable=True)
        self.set_skill(trigger_ids=[440], enable=True)
        self.set_skill(trigger_ids=[441], enable=True)
        self.set_skill(trigger_ids=[442], enable=True)
        self.set_skill(trigger_ids=[443], enable=True)
        self.set_skill(trigger_ids=[444], enable=True)
        self.set_skill(trigger_ids=[445], enable=True)
        self.set_skill(trigger_ids=[446], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬23대기(self.ctx)


class 스킬23대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[429])
        self.set_skill(trigger_ids=[430])
        self.set_skill(trigger_ids=[431])
        self.set_skill(trigger_ids=[432])
        self.set_skill(trigger_ids=[433])
        self.set_skill(trigger_ids=[434])
        self.set_skill(trigger_ids=[435])
        self.set_skill(trigger_ids=[436])
        self.set_skill(trigger_ids=[437])
        self.set_skill(trigger_ids=[438])
        self.set_skill(trigger_ids=[439])
        self.set_skill(trigger_ids=[440])
        self.set_skill(trigger_ids=[441])
        self.set_skill(trigger_ids=[442])
        self.set_skill(trigger_ids=[443])
        self.set_skill(trigger_ids=[444])
        self.set_skill(trigger_ids=[445])
        self.set_skill(trigger_ids=[446])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬23(self.ctx)


class 스킬23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[435], enable=True)
        self.set_skill(trigger_ids=[436], enable=True)
        self.set_skill(trigger_ids=[437], enable=True)
        self.set_skill(trigger_ids=[438], enable=True)
        self.set_skill(trigger_ids=[439], enable=True)
        self.set_skill(trigger_ids=[440], enable=True)
        self.set_skill(trigger_ids=[441], enable=True)
        self.set_skill(trigger_ids=[442], enable=True)
        self.set_skill(trigger_ids=[443], enable=True)
        self.set_skill(trigger_ids=[444], enable=True)
        self.set_skill(trigger_ids=[445], enable=True)
        self.set_skill(trigger_ids=[446], enable=True)
        self.set_skill(trigger_ids=[447], enable=True)
        self.set_skill(trigger_ids=[448], enable=True)
        self.set_skill(trigger_ids=[449], enable=True)
        self.set_skill(trigger_ids=[450], enable=True)
        self.set_skill(trigger_ids=[451], enable=True)
        self.set_skill(trigger_ids=[452], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬24대기(self.ctx)


class 스킬24대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[435])
        self.set_skill(trigger_ids=[436])
        self.set_skill(trigger_ids=[437])
        self.set_skill(trigger_ids=[438])
        self.set_skill(trigger_ids=[439])
        self.set_skill(trigger_ids=[440])
        self.set_skill(trigger_ids=[441])
        self.set_skill(trigger_ids=[442])
        self.set_skill(trigger_ids=[443])
        self.set_skill(trigger_ids=[444])
        self.set_skill(trigger_ids=[445])
        self.set_skill(trigger_ids=[446])
        self.set_skill(trigger_ids=[447])
        self.set_skill(trigger_ids=[448])
        self.set_skill(trigger_ids=[449])
        self.set_skill(trigger_ids=[450])
        self.set_skill(trigger_ids=[451])
        self.set_skill(trigger_ids=[452])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬24(self.ctx)


class 스킬24(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[441], enable=True)
        self.set_skill(trigger_ids=[442], enable=True)
        self.set_skill(trigger_ids=[443], enable=True)
        self.set_skill(trigger_ids=[444], enable=True)
        self.set_skill(trigger_ids=[445], enable=True)
        self.set_skill(trigger_ids=[446], enable=True)
        self.set_skill(trigger_ids=[447], enable=True)
        self.set_skill(trigger_ids=[448], enable=True)
        self.set_skill(trigger_ids=[449], enable=True)
        self.set_skill(trigger_ids=[450], enable=True)
        self.set_skill(trigger_ids=[451], enable=True)
        self.set_skill(trigger_ids=[452], enable=True)
        self.set_skill(trigger_ids=[453], enable=True)
        self.set_skill(trigger_ids=[454], enable=True)
        self.set_skill(trigger_ids=[455], enable=True)
        self.set_skill(trigger_ids=[456], enable=True)
        self.set_skill(trigger_ids=[457], enable=True)
        self.set_skill(trigger_ids=[458], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬25대기(self.ctx)


class 스킬25대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[441])
        self.set_skill(trigger_ids=[442])
        self.set_skill(trigger_ids=[443])
        self.set_skill(trigger_ids=[444])
        self.set_skill(trigger_ids=[445])
        self.set_skill(trigger_ids=[446])
        self.set_skill(trigger_ids=[447])
        self.set_skill(trigger_ids=[448])
        self.set_skill(trigger_ids=[449])
        self.set_skill(trigger_ids=[450])
        self.set_skill(trigger_ids=[451])
        self.set_skill(trigger_ids=[452])
        self.set_skill(trigger_ids=[453])
        self.set_skill(trigger_ids=[454])
        self.set_skill(trigger_ids=[455])
        self.set_skill(trigger_ids=[456])
        self.set_skill(trigger_ids=[457])
        self.set_skill(trigger_ids=[458])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬25(self.ctx)


class 스킬25(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[447], enable=True)
        self.set_skill(trigger_ids=[448], enable=True)
        self.set_skill(trigger_ids=[449], enable=True)
        self.set_skill(trigger_ids=[450], enable=True)
        self.set_skill(trigger_ids=[451], enable=True)
        self.set_skill(trigger_ids=[452], enable=True)
        self.set_skill(trigger_ids=[453], enable=True)
        self.set_skill(trigger_ids=[454], enable=True)
        self.set_skill(trigger_ids=[455], enable=True)
        self.set_skill(trigger_ids=[456], enable=True)
        self.set_skill(trigger_ids=[457], enable=True)
        self.set_skill(trigger_ids=[458], enable=True)
        self.set_skill(trigger_ids=[459], enable=True)
        self.set_skill(trigger_ids=[460], enable=True)
        self.set_skill(trigger_ids=[461], enable=True)
        self.set_skill(trigger_ids=[462], enable=True)
        self.set_skill(trigger_ids=[463], enable=True)
        self.set_skill(trigger_ids=[464], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬26대기(self.ctx)


class 스킬26대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[447])
        self.set_skill(trigger_ids=[448])
        self.set_skill(trigger_ids=[449])
        self.set_skill(trigger_ids=[450])
        self.set_skill(trigger_ids=[451])
        self.set_skill(trigger_ids=[452])
        self.set_skill(trigger_ids=[453])
        self.set_skill(trigger_ids=[454])
        self.set_skill(trigger_ids=[455])
        self.set_skill(trigger_ids=[456])
        self.set_skill(trigger_ids=[457])
        self.set_skill(trigger_ids=[458])
        self.set_skill(trigger_ids=[459])
        self.set_skill(trigger_ids=[460])
        self.set_skill(trigger_ids=[461])
        self.set_skill(trigger_ids=[462])
        self.set_skill(trigger_ids=[463])
        self.set_skill(trigger_ids=[464])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬26(self.ctx)


class 스킬26(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[453], enable=True)
        self.set_skill(trigger_ids=[454], enable=True)
        self.set_skill(trigger_ids=[455], enable=True)
        self.set_skill(trigger_ids=[456], enable=True)
        self.set_skill(trigger_ids=[457], enable=True)
        self.set_skill(trigger_ids=[458], enable=True)
        self.set_skill(trigger_ids=[459], enable=True)
        self.set_skill(trigger_ids=[460], enable=True)
        self.set_skill(trigger_ids=[461], enable=True)
        self.set_skill(trigger_ids=[462], enable=True)
        self.set_skill(trigger_ids=[463], enable=True)
        self.set_skill(trigger_ids=[464], enable=True)
        self.set_skill(trigger_ids=[465], enable=True)
        self.set_skill(trigger_ids=[466], enable=True)
        self.set_skill(trigger_ids=[467], enable=True)
        self.set_skill(trigger_ids=[468], enable=True)
        self.set_skill(trigger_ids=[469], enable=True)
        self.set_skill(trigger_ids=[470], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬27대기(self.ctx)


class 스킬27대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[453])
        self.set_skill(trigger_ids=[454])
        self.set_skill(trigger_ids=[455])
        self.set_skill(trigger_ids=[456])
        self.set_skill(trigger_ids=[457])
        self.set_skill(trigger_ids=[458])
        self.set_skill(trigger_ids=[459])
        self.set_skill(trigger_ids=[460])
        self.set_skill(trigger_ids=[461])
        self.set_skill(trigger_ids=[462])
        self.set_skill(trigger_ids=[463])
        self.set_skill(trigger_ids=[464])
        self.set_skill(trigger_ids=[465])
        self.set_skill(trigger_ids=[466])
        self.set_skill(trigger_ids=[467])
        self.set_skill(trigger_ids=[468])
        self.set_skill(trigger_ids=[469])
        self.set_skill(trigger_ids=[470])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬27(self.ctx)


class 스킬27(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[459], enable=True)
        self.set_skill(trigger_ids=[460], enable=True)
        self.set_skill(trigger_ids=[461], enable=True)
        self.set_skill(trigger_ids=[462], enable=True)
        self.set_skill(trigger_ids=[463], enable=True)
        self.set_skill(trigger_ids=[464], enable=True)
        self.set_skill(trigger_ids=[465], enable=True)
        self.set_skill(trigger_ids=[466], enable=True)
        self.set_skill(trigger_ids=[467], enable=True)
        self.set_skill(trigger_ids=[468], enable=True)
        self.set_skill(trigger_ids=[469], enable=True)
        self.set_skill(trigger_ids=[470], enable=True)
        self.set_skill(trigger_ids=[471], enable=True)
        self.set_skill(trigger_ids=[472], enable=True)
        self.set_skill(trigger_ids=[473], enable=True)
        self.set_skill(trigger_ids=[474], enable=True)
        self.set_skill(trigger_ids=[475], enable=True)
        self.set_skill(trigger_ids=[476], enable=True)
        self.set_skill(trigger_ids=[477], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬28대기(self.ctx)


class 스킬28대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[459])
        self.set_skill(trigger_ids=[460])
        self.set_skill(trigger_ids=[461])
        self.set_skill(trigger_ids=[462])
        self.set_skill(trigger_ids=[463])
        self.set_skill(trigger_ids=[464])
        self.set_skill(trigger_ids=[465])
        self.set_skill(trigger_ids=[466])
        self.set_skill(trigger_ids=[467])
        self.set_skill(trigger_ids=[468])
        self.set_skill(trigger_ids=[469])
        self.set_skill(trigger_ids=[470])
        self.set_skill(trigger_ids=[471])
        self.set_skill(trigger_ids=[472])
        self.set_skill(trigger_ids=[473])
        self.set_skill(trigger_ids=[474])
        self.set_skill(trigger_ids=[475])
        self.set_skill(trigger_ids=[476])
        self.set_skill(trigger_ids=[477])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬28(self.ctx)


class 스킬28(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[465], enable=True)
        self.set_skill(trigger_ids=[466], enable=True)
        self.set_skill(trigger_ids=[467], enable=True)
        self.set_skill(trigger_ids=[468], enable=True)
        self.set_skill(trigger_ids=[469], enable=True)
        self.set_skill(trigger_ids=[470], enable=True)
        self.set_skill(trigger_ids=[471], enable=True)
        self.set_skill(trigger_ids=[472], enable=True)
        self.set_skill(trigger_ids=[473], enable=True)
        self.set_skill(trigger_ids=[474], enable=True)
        self.set_skill(trigger_ids=[475], enable=True)
        self.set_skill(trigger_ids=[476], enable=True)
        self.set_skill(trigger_ids=[477], enable=True)
        self.set_skill(trigger_ids=[478], enable=True)
        self.set_skill(trigger_ids=[479], enable=True)
        self.set_skill(trigger_ids=[480], enable=True)
        self.set_skill(trigger_ids=[481], enable=True)
        self.set_skill(trigger_ids=[482], enable=True)
        self.set_skill(trigger_ids=[483], enable=True)
        self.set_skill(trigger_ids=[484], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬29대기(self.ctx)


class 스킬29대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[465])
        self.set_skill(trigger_ids=[466])
        self.set_skill(trigger_ids=[467])
        self.set_skill(trigger_ids=[468])
        self.set_skill(trigger_ids=[469])
        self.set_skill(trigger_ids=[470])
        self.set_skill(trigger_ids=[471])
        self.set_skill(trigger_ids=[472])
        self.set_skill(trigger_ids=[473])
        self.set_skill(trigger_ids=[474])
        self.set_skill(trigger_ids=[475])
        self.set_skill(trigger_ids=[476])
        self.set_skill(trigger_ids=[477])
        self.set_skill(trigger_ids=[478])
        self.set_skill(trigger_ids=[479])
        self.set_skill(trigger_ids=[480])
        self.set_skill(trigger_ids=[481])
        self.set_skill(trigger_ids=[482])
        self.set_skill(trigger_ids=[483])
        self.set_skill(trigger_ids=[484])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬29(self.ctx)


class 스킬29(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[471], enable=True)
        self.set_skill(trigger_ids=[472], enable=True)
        self.set_skill(trigger_ids=[473], enable=True)
        self.set_skill(trigger_ids=[474], enable=True)
        self.set_skill(trigger_ids=[475], enable=True)
        self.set_skill(trigger_ids=[476], enable=True)
        self.set_skill(trigger_ids=[477], enable=True)
        self.set_skill(trigger_ids=[478], enable=True)
        self.set_skill(trigger_ids=[479], enable=True)
        self.set_skill(trigger_ids=[480], enable=True)
        self.set_skill(trigger_ids=[481], enable=True)
        self.set_skill(trigger_ids=[482], enable=True)
        self.set_skill(trigger_ids=[483], enable=True)
        self.set_skill(trigger_ids=[484], enable=True)
        self.set_skill(trigger_ids=[485], enable=True)
        self.set_skill(trigger_ids=[486], enable=True)
        self.set_skill(trigger_ids=[487], enable=True)
        self.set_skill(trigger_ids=[488], enable=True)
        self.set_skill(trigger_ids=[489], enable=True)
        self.set_skill(trigger_ids=[490], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬30대기(self.ctx)


class 스킬30대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[471])
        self.set_skill(trigger_ids=[472])
        self.set_skill(trigger_ids=[473])
        self.set_skill(trigger_ids=[474])
        self.set_skill(trigger_ids=[475])
        self.set_skill(trigger_ids=[476])
        self.set_skill(trigger_ids=[477])
        self.set_skill(trigger_ids=[478])
        self.set_skill(trigger_ids=[479])
        self.set_skill(trigger_ids=[480])
        self.set_skill(trigger_ids=[481])
        self.set_skill(trigger_ids=[482])
        self.set_skill(trigger_ids=[483])
        self.set_skill(trigger_ids=[484])
        self.set_skill(trigger_ids=[485])
        self.set_skill(trigger_ids=[486])
        self.set_skill(trigger_ids=[487])
        self.set_skill(trigger_ids=[488])
        self.set_skill(trigger_ids=[489])
        self.set_skill(trigger_ids=[490])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬30(self.ctx)


class 스킬30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[478], enable=True)
        self.set_skill(trigger_ids=[479], enable=True)
        self.set_skill(trigger_ids=[480], enable=True)
        self.set_skill(trigger_ids=[481], enable=True)
        self.set_skill(trigger_ids=[482], enable=True)
        self.set_skill(trigger_ids=[483], enable=True)
        self.set_skill(trigger_ids=[484], enable=True)
        self.set_skill(trigger_ids=[485], enable=True)
        self.set_skill(trigger_ids=[486], enable=True)
        self.set_skill(trigger_ids=[487], enable=True)
        self.set_skill(trigger_ids=[488], enable=True)
        self.set_skill(trigger_ids=[489], enable=True)
        self.set_skill(trigger_ids=[490], enable=True)
        self.set_skill(trigger_ids=[491], enable=True)
        self.set_skill(trigger_ids=[492], enable=True)
        self.set_skill(trigger_ids=[493], enable=True)
        self.set_skill(trigger_ids=[494], enable=True)
        self.set_skill(trigger_ids=[495], enable=True)
        self.set_skill(trigger_ids=[496], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬31대기(self.ctx)


class 스킬31대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[478])
        self.set_skill(trigger_ids=[479])
        self.set_skill(trigger_ids=[480])
        self.set_skill(trigger_ids=[481])
        self.set_skill(trigger_ids=[482])
        self.set_skill(trigger_ids=[483])
        self.set_skill(trigger_ids=[484])
        self.set_skill(trigger_ids=[485])
        self.set_skill(trigger_ids=[486])
        self.set_skill(trigger_ids=[487])
        self.set_skill(trigger_ids=[488])
        self.set_skill(trigger_ids=[489])
        self.set_skill(trigger_ids=[490])
        self.set_skill(trigger_ids=[491])
        self.set_skill(trigger_ids=[492])
        self.set_skill(trigger_ids=[493])
        self.set_skill(trigger_ids=[494])
        self.set_skill(trigger_ids=[495])
        self.set_skill(trigger_ids=[496])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬31(self.ctx)


class 스킬31(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[485], enable=True)
        self.set_skill(trigger_ids=[486], enable=True)
        self.set_skill(trigger_ids=[487], enable=True)
        self.set_skill(trigger_ids=[488], enable=True)
        self.set_skill(trigger_ids=[489], enable=True)
        self.set_skill(trigger_ids=[490], enable=True)
        self.set_skill(trigger_ids=[491], enable=True)
        self.set_skill(trigger_ids=[492], enable=True)
        self.set_skill(trigger_ids=[493], enable=True)
        self.set_skill(trigger_ids=[494], enable=True)
        self.set_skill(trigger_ids=[495], enable=True)
        self.set_skill(trigger_ids=[496], enable=True)
        self.set_skill(trigger_ids=[497], enable=True)
        self.set_skill(trigger_ids=[498], enable=True)
        self.set_skill(trigger_ids=[499], enable=True)
        self.set_skill(trigger_ids=[500], enable=True)
        self.set_skill(trigger_ids=[501], enable=True)
        self.set_skill(trigger_ids=[502], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬32대기(self.ctx)


class 스킬32대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[485])
        self.set_skill(trigger_ids=[486])
        self.set_skill(trigger_ids=[487])
        self.set_skill(trigger_ids=[488])
        self.set_skill(trigger_ids=[489])
        self.set_skill(trigger_ids=[490])
        self.set_skill(trigger_ids=[491])
        self.set_skill(trigger_ids=[492])
        self.set_skill(trigger_ids=[493])
        self.set_skill(trigger_ids=[494])
        self.set_skill(trigger_ids=[495])
        self.set_skill(trigger_ids=[496])
        self.set_skill(trigger_ids=[497])
        self.set_skill(trigger_ids=[498])
        self.set_skill(trigger_ids=[499])
        self.set_skill(trigger_ids=[500])
        self.set_skill(trigger_ids=[501])
        self.set_skill(trigger_ids=[502])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬32(self.ctx)


class 스킬32(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[491], enable=True)
        self.set_skill(trigger_ids=[492], enable=True)
        self.set_skill(trigger_ids=[493], enable=True)
        self.set_skill(trigger_ids=[494], enable=True)
        self.set_skill(trigger_ids=[495], enable=True)
        self.set_skill(trigger_ids=[496], enable=True)
        self.set_skill(trigger_ids=[497], enable=True)
        self.set_skill(trigger_ids=[498], enable=True)
        self.set_skill(trigger_ids=[499], enable=True)
        self.set_skill(trigger_ids=[500], enable=True)
        self.set_skill(trigger_ids=[501], enable=True)
        self.set_skill(trigger_ids=[502], enable=True)
        self.set_skill(trigger_ids=[503], enable=True)
        self.set_skill(trigger_ids=[504], enable=True)
        self.set_skill(trigger_ids=[505], enable=True)
        self.set_skill(trigger_ids=[506], enable=True)
        self.set_skill(trigger_ids=[507], enable=True)
        self.set_skill(trigger_ids=[508], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 스킬33대기(self.ctx)


class 스킬33대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1')
        self.set_skill(trigger_ids=[491])
        self.set_skill(trigger_ids=[492])
        self.set_skill(trigger_ids=[493])
        self.set_skill(trigger_ids=[494])
        self.set_skill(trigger_ids=[495])
        self.set_skill(trigger_ids=[496])
        self.set_skill(trigger_ids=[497])
        self.set_skill(trigger_ids=[498])
        self.set_skill(trigger_ids=[499])
        self.set_skill(trigger_ids=[500])
        self.set_skill(trigger_ids=[501])
        self.set_skill(trigger_ids=[502])
        self.set_skill(trigger_ids=[503])
        self.set_skill(trigger_ids=[504])
        self.set_skill(trigger_ids=[505])
        self.set_skill(trigger_ids=[506])
        self.set_skill(trigger_ids=[507])
        self.set_skill(trigger_ids=[508])

    def on_tick(self) -> trigger_api.Trigger:
        return 스킬33(self.ctx)


class 스킬33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_skill(trigger_ids=[497], enable=True)
        self.set_skill(trigger_ids=[498], enable=True)
        self.set_skill(trigger_ids=[499], enable=True)
        self.set_skill(trigger_ids=[500], enable=True)
        self.set_skill(trigger_ids=[501], enable=True)
        self.set_skill(trigger_ids=[502], enable=True)
        self.set_skill(trigger_ids=[503], enable=True)
        self.set_skill(trigger_ids=[504], enable=True)
        self.set_skill(trigger_ids=[505], enable=True)
        self.set_skill(trigger_ids=[506], enable=True)
        self.set_skill(trigger_ids=[507], enable=True)
        self.set_skill(trigger_ids=[508], enable=True)
        self.set_skill(trigger_ids=[509], enable=True)
        self.set_skill(trigger_ids=[510], enable=True)
        self.set_skill(trigger_ids=[511], enable=True)
        self.set_skill(trigger_ids=[512], enable=True)
        self.set_skill(trigger_ids=[513], enable=True)
        self.set_skill(trigger_ids=[514], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[497])
        self.set_skill(trigger_ids=[498])
        self.set_skill(trigger_ids=[499])
        self.set_skill(trigger_ids=[500])
        self.set_skill(trigger_ids=[501])
        self.set_skill(trigger_ids=[502])
        self.set_skill(trigger_ids=[503])
        self.set_skill(trigger_ids=[504])
        self.set_skill(trigger_ids=[505])
        self.set_skill(trigger_ids=[506])
        self.set_skill(trigger_ids=[507])
        self.set_skill(trigger_ids=[508])
        self.set_skill(trigger_ids=[509])
        self.set_skill(trigger_ids=[510])
        self.set_skill(trigger_ids=[511])
        self.set_skill(trigger_ids=[512])
        self.set_skill(trigger_ids=[513])
        self.set_skill(trigger_ids=[514])


initial_state = 대기
