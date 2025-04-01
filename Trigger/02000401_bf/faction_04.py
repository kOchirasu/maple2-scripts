""" trigger/02000401_bf/faction_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601])
        self.remove_buff(box_id=199, skill_id=99910160)
        self.set_interact_object(trigger_ids=[12000029], state=2)
        self.set_interact_object(trigger_ids=[12000040], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='faction04') == 1:
            return 인원수체크(self.ctx)


class 인원수체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip(state=반응대기)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawn_ids=[2902])
        # self.set_cinematic_ui(type=1)
        # self.set_cinematic_ui(type=3)
        self.add_buff(box_ids=[199], skill_id=70000107, level=1, ignore_player=False, is_skill_set=False)
        self.select_camera(trigger_id=303)
        self.spawn_monster(spawn_ids=[1300])
        self.spawn_monster(spawn_ids=[1301,1302,1303,1304,1305], auto_target=False)
        self.set_dialogue(type=1, spawn_id=1301, script='$02000401_BF__FACTION_04__0$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 반응대기(self.ctx)


class 반응대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skip() # Missing State: State
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.show_guide_summary(entity_id=20040104, text_id=20040104, duration=2500)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.remove_buff(box_id=199, skill_id=70000107)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera()

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NPClanding') == 1:
            return 룸체크(self.ctx)


class 룸체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return 던전(self.ctx)
        if not self.is_dungeon_room():
            return 퀘스트(self.ctx)


class 던전(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000029], state=1)
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 보스소환(self.ctx)


class 퀘스트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[12000040], state=1)
        self.set_effect(trigger_ids=[601], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 보스소환(self.ctx)


class 보스소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.show_guide_summary(entity_id=20040107, text_id=20040107, duration=3000)
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.spawn_monster(spawn_ids=[2099], auto_target=False)
        self.set_user_value(trigger_id=99999100, key='bossSpawn', value=1)
        self.destroy_monster(spawn_ids=[1300], arg2=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='DungeonClear') == 1:
            self.destroy_monster(spawn_ids=[1300,1301,1302,1303,1304,1305], arg2=False)
            self.set_interact_object(trigger_ids=[12000029], state=0)
            self.set_interact_object(trigger_ids=[12000040], state=0)
            self.remove_buff(box_id=199, skill_id=99910160)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
