""" trigger/02000290_bf/main_2.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[905], visible=True)
        self.set_agent(trigger_ids=[906], visible=True)
        self.set_agent(trigger_ids=[907], visible=True)
        self.set_agent(trigger_ids=[908], visible=True)
        self.set_ladder(trigger_ids=[531])
        self.set_ladder(trigger_ids=[532])
        self.set_ladder(trigger_ids=[533])
        self.set_ladder(trigger_ids=[534])
        self.set_ladder(trigger_ids=[535])
        self.set_ladder(trigger_ids=[536])
        self.set_mesh(trigger_ids=[3089], visible=True)
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107])
        self.set_mesh(trigger_ids=[3108], visible=True)
        self.set_actor(trigger_id=3110, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3111], visible=True)
        self.set_mesh(trigger_ids=[3112,3113,3114,3115,3116,3117], visible=True)
        self.set_actor(trigger_id=3120, visible=True, initial_sequence='Closed')
        self.set_mesh(trigger_ids=[3121], visible=True)
        self.set_mesh(trigger_ids=[3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132], visible=True)
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209])
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504], visible=True)
        self.set_effect(trigger_ids=[5101]) # LadderAppear
        self.destroy_monster(spawn_ids=[1011])
        self.destroy_monster(spawn_ids=[1012])
        self.destroy_monster(spawn_ids=[1013])
        self.destroy_monster(spawn_ids=[1014])
        self.destroy_monster(spawn_ids=[1015])
        self.destroy_monster(spawn_ids=[1016])
        self.destroy_monster(spawn_ids=[1017])
        self.destroy_monster(spawn_ids=[1018])
        self.destroy_monster(spawn_ids=[1019])
        self.set_portal(portal_id=2)
        self.set_effect(trigger_ids=[6003])
        self.set_effect(trigger_ids=[6004])
        self.set_effect(trigger_ids=[6005])
        self.set_effect(trigger_ids=[6006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101]):
            return 준비(self.ctx)


class 준비(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2001], auto_target=False)
        self.spawn_monster(spawn_ids=[2002], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 사다리생성(self.ctx)


class 사다리생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.show_guide_summary(entity_id=20002903, text_id=20002903)
        self.set_effect(trigger_ids=[5101], visible=True) # LadderAppear
        self.set_ladder(trigger_ids=[531], visible=True, enable=True)
        self.set_ladder(trigger_ids=[532], visible=True, enable=True)
        self.set_ladder(trigger_ids=[533], visible=True, enable=True)
        self.set_ladder(trigger_ids=[534], visible=True, enable=True)
        self.set_ladder(trigger_ids=[535], visible=True, enable=True)
        self.set_ladder(trigger_ids=[536], visible=True, enable=True)
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=9991, is_enable=True)
        self.enable_spawn_point_pc(spawn_id=9992)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.hide_guide_summary(entity_id=20002903)
            return 트리거09시작(self.ctx)


class 트리거09시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[1011], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1011]):
            return 트리거10시작(self.ctx)
        if self.wait_tick(wait_tick=10000):
            return 트리거10시작(self.ctx)


class 트리거10시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[905])
        self.set_agent(trigger_ids=[906])
        self.set_mesh(trigger_ids=[3089])
        self.set_mesh(trigger_ids=[3200,3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=True, interval=200, fade=2.0)
        self.spawn_monster(spawn_ids=[1012], auto_target=False)
        self.spawn_monster(spawn_ids=[1013], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1012,1013]):
            return 트리거11시작(self.ctx)
        if self.wait_tick(wait_tick=12000):
            return 트리거11시작(self.ctx)


class 트리거11시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_agent(trigger_ids=[907])
        self.set_agent(trigger_ids=[908])
        self.set_mesh(trigger_ids=[3108])
        self.set_mesh(trigger_ids=[3100,3101,3102,3103,3104,3105,3106,3107], visible=True, interval=200, fade=2.0)
        self.spawn_monster(spawn_ids=[1014], auto_target=False)
        self.spawn_monster(spawn_ids=[1015], auto_target=False)
        self.spawn_monster(spawn_ids=[1016], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1014,1015,1016]):
            return 트리거12시작(self.ctx)
        if self.wait_tick(wait_tick=15000):
            return 트리거12시작(self.ctx)


class 트리거12시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3110, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3111])
        self.spawn_monster(spawn_ids=[1017], auto_target=False)
        self.spawn_monster(spawn_ids=[1018], auto_target=False)
        self.spawn_monster(spawn_ids=[1019], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리거12진행(self.ctx)


class 트리거12진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3110, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3112,3113,3114,3115,3116,3117], interval=200, fade=2.0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[1017,1018,1019]):
            return 트리거13시작(self.ctx)
        if self.wait_tick(wait_tick=15000):
            return 트리거13시작(self.ctx)


class 트리거13시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3120, visible=True, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3121])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 트리거13진행(self.ctx)


class 트리거13진행(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(trigger_id=3120, initial_sequence='Opened')
        self.set_mesh(trigger_ids=[3122,3123,3124,3125,3126,3127,3128,3129,3130,3131,3132], interval=200, fade=2.0)
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=9991)
        self.enable_spawn_point_pc(spawn_id=9992, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2002]):
            return 연출대기(self.ctx)


class 연출대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='3', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(trigger_id=801)
        self.set_timer(timer_id='3', seconds=3)
        self.set_mesh(trigger_ids=[3500,3501,3502,3503,3504], interval=300, fade=3.0)
        self.set_skip(state=연출종료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='3'):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(path_ids=[801])
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return 공주구출(self.ctx)


class 공주구출(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=801, enable=False)
        self.set_effect(trigger_ids=[5000], visible=True) # GuideUI
        self.show_guide_summary(entity_id=20002904, text_id=20002904)
        self.set_interact_object(trigger_ids=[10000464], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000464], state=0):
            self.hide_guide_summary(entity_id=20002904)
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=7, arg2='$02000290_BF__MAIN_2__2$', arg3='3000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 포털생성(self.ctx)


class 포털생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[910])
        self.spawn_monster(spawn_ids=[911])
        self.spawn_monster(spawn_ids=[912])
        self.spawn_monster(spawn_ids=[913])
        self.spawn_monster(spawn_ids=[914])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC이동01(self.ctx)


class NPC이동01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=910, patrol_name='MS2PatrolData910')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC이동02(self.ctx)


class NPC이동02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=911, patrol_name='MS2PatrolData911')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC이동03(self.ctx)


class NPC이동03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=912, patrol_name='MS2PatrolData912')
        self.move_npc(spawn_id=914, patrol_name='MS2PatrolData914')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC이동04(self.ctx)


class NPC이동04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=913, patrol_name='MS2PatrolData913')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return NPC대사01(self.ctx)


class NPC대사01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.set_dialogue(type=1, spawn_id=910, script='$02000290_BF__MAIN_2__4$', time=3)
            self.set_effect(trigger_ids=[6003], visible=True)
            return NPC대사02(self.ctx)


class NPC대사02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_dialogue(type=1, spawn_id=911, script='$02000290_BF__MAIN_2__5$', time=3)
            self.set_effect(trigger_ids=[6004], visible=True)
            return NPC대사03(self.ctx)


class NPC대사03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_dialogue(type=1, spawn_id=912, script='$02000290_BF__MAIN_2__6$', time=3)
            self.set_effect(trigger_ids=[6005], visible=True)
            return NPC대사04(self.ctx)


class NPC대사04(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            self.set_dialogue(type=1, spawn_id=913, script='$02000290_BF__MAIN_2__7$', time=3)
            self.set_effect(trigger_ids=[6006], visible=True)
            self.hide_guide_summary(entity_id=20002905)
            return 종료대기(self.ctx)


class 종료대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.dungeon_clear()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=99999, type='trigger', achieve='ClearYomiprincess') # ClearYomiprincess 퀘스트
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = 대기
