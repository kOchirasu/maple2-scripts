""" trigger/52000188_qd/52000188.xml """
import trigger_api


class wait_01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002794], quest_states=[2]):
            return 바베니로_01(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2]):
            return 컷씬준비(self.ctx)
        if self.user_detected(box_ids=[2001], job_code=0):
            return wait_01_02(self.ctx)


class wait_01_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)
        self.move_user(map_id=52000188, portal_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 동굴도착_01(self.ctx)


class 동굴도착_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 동굴도착_01_2(self.ctx)


class 동굴도착_01_2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[4001,4002], return_view=False)
        self.move_user_path(patrol_name='MS2PatrolData_3001')
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 동굴도착_02(self.ctx)


class 동굴도착_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=3)
        self.add_cinematic_talk(npc_id=0, msg='$52000188_QD__52000188__0$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 정리_01(self.ctx)


class 정리_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_scene_skip() # Missing State: State

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 정리_02(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=1, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_CameraMasking_SlowFade.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 정리_02(self.ctx)


class 정리_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 밝아짐(self.ctx)


class 밝아짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=2, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2]):
            return 컷씬준비(self.ctx)


# 직업별 컷씬 출력
class 컷씬준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 컷씬준비_02(self.ctx)


class 컷씬준비_02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=10):
            return 나이트컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=20):
            return 버서커컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=30):
            return 위자드컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=40):
            return 프리스트컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=50):
            return 레인저컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=60):
            return 헤비거너컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=70):
            return 시프컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=80):
            return 어쌔신컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=90):
            return 룬블컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=100):
            return 스커컷씬(self.ctx)
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002793], quest_states=[2], job_code=110):
            return 소바컷씬(self.ctx)


class 나이트컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_knight.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 버서커컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_berserker.swf', movie_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 위자드컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_wizard.swf', movie_id=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 프리스트컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_priest.swf', movie_id=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 레인저컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_ranger.swf', movie_id=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 헤비거너컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_heavy.swf', movie_id=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 시프컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_thief.swf', movie_id=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 어쌔신컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_Assassin.swf', movie_id=8)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 룬블컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_RBlader.swf', movie_id=9)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 스커컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_striker.swf', movie_id=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 소바컷씬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.play_scene_movie(file_name='MasterSkill_soul.swf', movie_id=11)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return 영상재생_end(self.ctx)
        if self.wait_tick(wait_tick=5000):
            return 영상재생_end(self.ctx)


class 영상재생_end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=30, path='BG/Common/ScreenMask/Eff_CameraMasking_FastWhiteOutFast.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 영상재생_end02(self.ctx)


class 영상재생_end02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[2001], quest_ids=[40002794], quest_states=[2]):
            return 바베니로_01(self.ctx)


class 바베니로_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        self.set_cinematic_ui(type=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 바베니로_02(self.ctx)


class 바베니로_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(map_id=2020041, portal_id=1)


initial_state = wait_01
