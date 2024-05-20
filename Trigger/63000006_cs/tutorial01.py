""" trigger/63000006_cs/tutorial01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_portal(portal_id=1, visible=True, minimap_visible=True)
        self.set_skill(trigger_ids=[900])
        self.set_skill(trigger_ids=[901])
        self.set_skill(trigger_ids=[902])
        self.set_skill(trigger_ids=[903])
        self.set_skill(trigger_ids=[904])
        self.set_skill(trigger_ids=[905])
        self.set_skill(trigger_ids=[906])
        self.set_skill(trigger_ids=[907])
        self.set_mesh(trigger_ids=[3000], visible=True) # bridge 1st barrier ON
        self.set_mesh(trigger_ids=[3001], visible=True) # bridge 2nd  barrier ON
        # bridge left guide barrier ON
        self.set_mesh(trigger_ids=[3002], visible=True)
        # bridge right guide barrier ON
        self.set_mesh(trigger_ids=[3003], visible=True)
        # bridge 3rd guide barrier OFF
        self.set_mesh(trigger_ids=[3004])
        self.set_effect(trigger_ids=[5011]) # bridge enter 01
        self.set_effect(trigger_ids=[5012]) # bridge enter 02
        self.set_effect(trigger_ids=[5013]) # bridge enter 03
        self.set_effect(trigger_ids=[5014]) # bridge enter 04
        self.set_effect(trigger_ids=[5015]) # bridge enter 05
        self.set_effect(trigger_ids=[5000]) # move point 1
        self.set_effect(trigger_ids=[5001]) # move point 2
        self.set_effect(trigger_ids=[5012]) # bridge enter 03
        self.set_effect(trigger_ids=[5013]) # bridge enter 04
        self.set_effect(trigger_ids=[5020]) # after swim 01
        self.set_effect(trigger_ids=[5021]) # after swim 02
        self.set_effect(trigger_ids=[5022]) # after swim 03
        self.set_effect(trigger_ids=[5023]) # after swim 04
        self.set_effect(trigger_ids=[5024]) # after swim 05
        self.set_effect(trigger_ids=[5025]) # after swim 06
        self.set_effect(trigger_ids=[5026]) # after swim 07
        self.set_effect(trigger_ids=[5027]) # after swim 08
        self.set_effect(trigger_ids=[5028]) # after swim 09
        self.set_effect(trigger_ids=[5040]) # toward portal 01
        self.set_effect(trigger_ids=[5041]) # toward portal 02
        self.set_effect(trigger_ids=[5042]) # toward portal 03
        self.set_effect(trigger_ids=[5043]) # toward portal 04
        self.set_effect(trigger_ids=[5044]) # toward portal 05
        self.set_effect(trigger_ids=[5045]) # toward portal 06
        self.set_effect(trigger_ids=[5046]) # toward portal 07
        self.set_effect(trigger_ids=[5047]) # toward portal 08
        self.set_effect(trigger_ids=[5048]) # toward portal 09
        self.set_effect(trigger_ids=[5050]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5051]) # 미션 완료 사운드 이펙트
        self.set_effect(trigger_ids=[5052]) # 화살표  안내 사운드 이펙트
        self.set_effect(trigger_ids=[5060]) # 이슈라 음성 사운드 이펙트 01
        self.set_effect(trigger_ids=[5061]) # 이슈라 음성 사운드 이펙트 02
        self.set_effect(trigger_ids=[5062]) # 이슈라 음성 사운드 이펙트 03
        self.set_effect(trigger_ids=[5063]) # 이슈라 음성 사운드 이펙트 04
        self.set_effect(trigger_ids=[5064]) # 이슈라 음성 사운드 이펙트 05
        self.set_effect(trigger_ids=[5065]) # 이슈라 음성 사운드 이펙트 06
        self.set_effect(trigger_ids=[5066]) # 이슈라 음성 사운드 이펙트 07
        self.set_effect(trigger_ids=[5080]) # 이슈라 다리 건널 때 삐걱 사운드 이펙트
        self.set_effect(trigger_ids=[5090]) # PC 물에 빠질 때 풍덩 사운드  이펙트
        self.spawn_monster(spawn_ids=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9000]):
            return 영상준비_01(self.ctx)


class 영상준비_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 영상재생_01(self.ctx)


class 영상재생_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\Common_Opening.usm', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 룬블영상준비_01(self.ctx)
        if self.wait_tick(wait_tick=190000):
            return 룬블영상준비_01(self.ctx)


class 룬블영상준비_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 룬블영상재생_01(self.ctx)


class 룬블영상재생_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='common\\RuneBlader_Intro.usm', movie_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 2:
            return 룬블영상완료_01(self.ctx)
        if self.wait_tick(wait_tick=30000):
            return 룬블영상완료_01(self.ctx)


class 룬블영상완료_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 키타입설정안내01(self.ctx)
        if self.user_detected(box_ids=[9050,9051,9052,9053]):
            return 로딩딜레이(self.ctx)


"""
class 영상딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='101', seconds=30)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='101'):
            return 플레이준비(self.ctx)
        if self.user_detected(box_ids=[9050,9051,9052,9053]):
            return 로딩딜레이(self.ctx)
"""

class 키타입설정안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(event_id=10010005) # 트리거 To가이드 : 키타입설정

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 10010009:
            # 가이드 To 트리거 - 키타입설정완료
            return 플레이준비(self.ctx)


class 플레이준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10010001, text_id=10010001) # 가이드 : 화살표 키를 눌러 움직이기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9050,9051,9052,9053]):
            return 로딩딜레이(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10010001)


class 로딩딜레이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='1'):
            return 기상준비01(self.ctx)


class 기상준비01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='2', seconds=1)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_999')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='2'):
            return 기상대화01(self.ctx)


class 기상대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=4)
        self.set_effect(trigger_ids=[5060], visible=True) # 이슈라 음성 사운드 이펙트 01
        self.set_dialogue(type=2, spawn_id=11001244, script='$63000006_CS__TUTORIAL01__0$', time=4)
        self.set_skip(state=움직이기01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 움직이기01(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 움직이기01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # 목표지점 바닥
        self.set_effect(trigger_ids=[5001], visible=True) # 목표지점 화살표
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entity_id=10010000, text_id=10010000) # 가이드 : 화살표 키를 눌러 움직이기

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[6001]):
            return 움직이기02(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5060]) # 이슈라 음성 사운드 이펙트 01


class 움직이기02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_998')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[6000]):
            return 이동완료01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5051], visible=True) # 미션 완료 사운드 이펙트
        self.hide_guide_summary(entity_id=10010000)


class 이동완료01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000]) # 목표지점 바닥
        self.set_effect(trigger_ids=[5001]) # 목표지점 화살표
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        return 이동전대화01(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5050]) # 가이드 서머리 사운드 이펙트


class 이동전대화01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        return 이동전대화02(self.ctx)


class 이동전대화02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='4', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001244, script='$63000006_CS__TUTORIAL01__1$', time=3)
        self.set_effect(trigger_ids=[5061], visible=True) # 이슈라 음성 사운드 이펙트 02

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='4'):
            return 이동전대화03(self.ctx)


class 이동전대화03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='5', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001244, script='$63000006_CS__TUTORIAL01__2$', time=3)
        self.set_effect(trigger_ids=[5061]) # 이슈라 음성 사운드 이펙트 02
        self.set_effect(trigger_ids=[5062], visible=True) # 이슈라 음성 사운드 이펙트 03
        self.set_skip(state=미니맵가이드01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='5'):
            return 미니맵가이드01(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


# 트리거 To가이드
class 미니맵가이드01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트리거 To가이드 : 탭키 눌러서 미니맵 크게 보기
        self.guide_event(event_id=10010010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='Guide', name='IsTriggerEvent') == 10010020:
            # 가이드 To 트리거 -: 미니맵 크게 보기 완료
            return 이슈라이동01(self.ctx)


class 이슈라이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='10', seconds=3)
        self.set_dialogue(type=1, spawn_id=101, script='$63000006_CS__TUTORIAL01__3$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='10'):
            return 이슈라이동02(self.ctx)


class 이슈라이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='11', seconds=1)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='11'):
            return 이슈라이동03(self.ctx)


class 이슈라이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='12', seconds=4)
        self.set_dialogue(type=1, spawn_id=101, script='$63000006_CS__TUTORIAL01__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='12'):
            return 이슈라이동04(self.ctx)


class 이슈라이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='13', seconds=4)
        self.set_dialogue(type=1, spawn_id=101, script='$63000006_CS__TUTORIAL01__5$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='13'):
            return 이슈라이동05(self.ctx)


class 이슈라이동05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='14', seconds=4)
        self.set_dialogue(type=1, spawn_id=101, script='$63000006_CS__TUTORIAL01__6$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='14'):
            return 다리연출준비(self.ctx)


class 다리연출준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8002, spawn_ids=[101]):
            return 다리연출01(self.ctx)


class 다리연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001244, script='$63000006_CS__TUTORIAL01__7$', time=3)
        self.set_effect(trigger_ids=[5064], visible=True) # 이슈라 음성 사운드 이펙트 05
        self.set_skip(state=다리연출02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return 다리연출02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 다리연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601)
        self.set_effect(trigger_ids=[5080], visible=True) # 이슈라 다리 건널 때 삐걱 사운드 이펙트
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8004, spawn_ids=[101]):
            return 다리연출03(self.ctx)


class 다리연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=601, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8005, spawn_ids=[101]):
            return 다리연출종료(self.ctx)


class 다리연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=101, script='$63000006_CS__TUTORIAL01__8$', time=3)
        self.set_effect(trigger_ids=[5080]) # 이슈라 다리 건널 때 삐걱 사운드 이펙트
        self.set_effect(trigger_ids=[5064]) # 이슈라 음성 사운드 이펙트 05
        self.set_effect(trigger_ids=[5011], visible=True) # bridge enter 01
        self.set_effect(trigger_ids=[5012], visible=True) # bridge enter 02
        self.set_effect(trigger_ids=[5013], visible=True) # bridge enter 03
        self.set_effect(trigger_ids=[5014], visible=True) # bridge enter 04
        self.set_effect(trigger_ids=[5015], visible=True) # bridge enter 05
        self.show_guide_summary(entity_id=10010020, text_id=10010020) # 가이드 : 이슈라에게 이동하기
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5052], visible=True) # 화살표  안내 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        return 다리붕괴01(self.ctx)


class 다리붕괴01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3000]) # 1st bridge barrier OFF

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9003]):
            return 다리붕괴02(self.ctx)

    def on_exit(self) -> None:
        # bridge 3rd guide barrier ON
        self.set_mesh(trigger_ids=[3004], visible=True)
        # bridge left guide barrier OFF
        self.set_mesh(trigger_ids=[3002])
        # bridge right guide barrier OFF
        self.set_mesh(trigger_ids=[3003])
        self.hide_guide_summary(entity_id=10010020)
        self.set_effect(trigger_ids=[5050]) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5052]) # 화살표  안내 사운드 이펙트
        self.set_effect(trigger_ids=[5011]) # bridge enter 01
        self.set_effect(trigger_ids=[5012]) # bridge enter 02
        self.set_effect(trigger_ids=[5013]) # bridge enter 03
        self.set_effect(trigger_ids=[5014]) # bridge enter 04
        self.set_effect(trigger_ids=[5015]) # bridge enter 05


class 다리붕괴02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[902], enable=True)
        self.set_skill(trigger_ids=[906], enable=True)
        self.set_effect(trigger_ids=[5090], visible=True) # PC 물에 빠질 때 풍덩 사운드  이펙트

    def on_tick(self) -> trigger_api.Trigger:
        return 다리붕괴03(self.ctx)


class 다리붕괴03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[900], enable=True)
        self.set_skill(trigger_ids=[904], enable=True)
        self.set_skill(trigger_ids=[901], enable=True)
        self.set_skill(trigger_ids=[905], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 다리붕괴04(self.ctx)


class 다리붕괴04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[903], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        return 다리붕괴05(self.ctx)


class 다리붕괴05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(trigger_ids=[907], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9004]):
            return 수영안내01(self.ctx)

    def on_exit(self) -> None:
        self.set_skill(trigger_ids=[901])
        self.set_skill(trigger_ids=[902])
        self.set_skill(trigger_ids=[903])
        self.set_mesh(trigger_ids=[3001]) # bridge barrier OFF
        # bridge 3rd guide barrier OFF
        self.set_mesh(trigger_ids=[3004])


class 수영안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[5090]) # PC 물에 빠질 때 풍덩 사운드  이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return 수영안내02(self.ctx)


class 수영안내02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=4)
        self.set_dialogue(type=2, spawn_id=11001244, script='$63000006_CS__TUTORIAL01__9$', time=3)
        self.set_effect(trigger_ids=[5065], visible=True) # 이슈라 음성 사운드 이펙트 06

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return 수영안내03(self.ctx)


class 수영안내03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='32', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001244, script='$63000006_CS__TUTORIAL01__10$', time=3)
        self.set_effect(trigger_ids=[5065]) # 이슈라 음성 사운드 이펙트 06
        self.set_effect(trigger_ids=[5066], visible=True) # 이슈라 음성 사운드 이펙트 07
        self.set_skip(state=이슈라교체)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='32'):
            return 이슈라교체(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class 이슈라교체(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10010030, text_id=10010030) # 가이드 : 방향키를 눌러 수영하기
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5020], visible=True) # after swim 01
        self.set_effect(trigger_ids=[5021], visible=True) # after swim 02
        self.set_effect(trigger_ids=[5022], visible=True) # after swim 03
        self.set_effect(trigger_ids=[5023], visible=True) # after swim 04
        self.set_effect(trigger_ids=[5024], visible=True) # after swim 05
        self.set_effect(trigger_ids=[5025], visible=True) # after swim 06
        self.set_effect(trigger_ids=[5026], visible=True) # after swim 07
        self.set_effect(trigger_ids=[5027], visible=True) # after swim 08
        self.set_effect(trigger_ids=[5028], visible=True) # after swim 09
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_npc(spawn_id=101, patrol_name='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8006, spawn_ids=[101]):
            return 연출05종료(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5066]) # 이슈라 음성 사운드 이펙트 07


class 연출05종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9010,9011,9012,9013,9014,9015]):
            return 사다리유도01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10010030)


class 사다리유도01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10010020, text_id=10010020) # 가이드 : 이슈라에게 이동하기
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9006]):
            return 사다리유도02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10010020)


class 사다리유도02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10010040, text_id=10010040) # 가이드 : ↑키를 눌러 사다리 올라가기
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5040], visible=True) # toward portal 01

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9005]):
            return 언덕유도01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10010040)


class 언덕유도01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10010020, text_id=10010020) # 가이드 : 이슈라에게 이동하기
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(trigger_ids=[5041], visible=True) # toward portal 02
        self.set_effect(trigger_ids=[5042], visible=True) # toward portal 03
        self.set_effect(trigger_ids=[5043], visible=True) # toward portal 04
        self.set_effect(trigger_ids=[5044], visible=True) # toward portal 05
        self.set_effect(trigger_ids=[5045], visible=True) # toward portal 06
        self.set_effect(trigger_ids=[5046], visible=True) # toward portal 07
        self.set_effect(trigger_ids=[5047], visible=True) # toward portal 08
        self.set_effect(trigger_ids=[5048], visible=True) # toward portal 09

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9020]):
            return 언덕유도02(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10010020)


class 언덕유도02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10010050, text_id=10010050) # 가이드 : C키로 점프하여 언덕 올라가기
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[9021]):
            return 퀘스트수락유도01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10010050)


class 퀘스트수락유도01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=10010060, text_id=10010060) # 가이드 : 이슈라와 대화해서 퀘스트 수락하기
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9030], quest_ids=[90000410], quest_states=[1]):
            # 유페리아 만나기  퀘스트 진행 중 상태
            return 포털생성01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entity_id=10010060)
        self.set_effect(trigger_ids=[5040]) # toward portal 01
        self.set_effect(trigger_ids=[5041]) # toward portal 02
        self.set_effect(trigger_ids=[5042]) # toward portal 03
        self.set_effect(trigger_ids=[5043]) # toward portal 04
        self.set_effect(trigger_ids=[5044]) # toward portal 05
        self.set_effect(trigger_ids=[5045]) # toward portal 06
        self.set_effect(trigger_ids=[5046]) # toward portal 07
        self.set_effect(trigger_ids=[5020]) # after swim 01
        self.set_effect(trigger_ids=[5021]) # after swim 02
        self.set_effect(trigger_ids=[5022]) # after swim 03
        self.set_effect(trigger_ids=[5023]) # after swim 04
        self.set_effect(trigger_ids=[5024]) # after swim 05
        self.set_effect(trigger_ids=[5025]) # after swim 06
        self.set_effect(trigger_ids=[5026]) # after swim 07
        self.set_effect(trigger_ids=[5027]) # after swim 08
        self.set_effect(trigger_ids=[5028]) # after swim 09


class 포털생성01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='35', seconds=1)
        self.set_portal(portal_id=1, visible=True, enable=True, minimap_visible=True)
        # 트리거 To가이드 : 포털 위에 노란색 화살표 타겟팅
        self.guide_event(event_id=10010080)
        self.show_guide_summary(entity_id=10010070, text_id=10010070) # 가이드 : 포털 위치에서 스페이스 키 누르기
        self.set_effect(trigger_ids=[5050], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='35'):
            return 이슈라퇴장01(self.ctx)


class 이슈라퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_dialogue(type=1, spawn_id=102, script='$63000006_CS__TUTORIAL01__11$', time=3)
        self.move_npc(spawn_id=102, patrol_name='MS2PatrolData_1004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8008, spawn_ids=[102]):
            return 이슈라퇴장02(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(trigger_ids=[5050]) # 가이드 서머리 사운드 이펙트


class 이슈라퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[102])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(box_ids=[9040]):
            # 맵 전체에 유저 없는지 체크
            return 맵이동완료(self.ctx)


class 맵이동완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entity_id=10010070)
        self.set_effect(trigger_ids=[5047]) # toward portal 08
        self.set_effect(trigger_ids=[5048]) # toward portal 09


initial_state = 대기
