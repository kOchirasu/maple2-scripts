""" trigger/52010005_qd/act03.xml """
import trigger_api


class 퀘스트조건03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000872], state=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002822], quest_states=[1]):
            # 3rd Quest
            return Q3_딜레이01(self.ctx)


class Q3_딜레이01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='100', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='100'):
            return Q3_미카등장01(self.ctx)


# 3rd Quest
class Q3_미카등장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='20', seconds=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.spawn_monster(spawn_ids=[601], auto_target=False)
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_6010')
        self.destroy_monster(spawn_ids=[401])
        self.destroy_monster(spawn_ids=[101])
        self.spawn_monster(spawn_ids=[501], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='20'):
            return Q3_미카연출01(self.ctx)


class Q3_미카연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='21', seconds=5)
        self.select_camera_path(path_ids=[2001,2002], return_view=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='21'):
            return Q3_미카연출02(self.ctx)


class Q3_미카연출02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8003, spawn_ids=[601]):
            return Q3_미카연출03(self.ctx)


class Q3_미카연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='22', seconds=4)
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_6011')
        self.select_camera_path(path_ids=[2002,2001])

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='22'):
            return Q3_미카연출04(self.ctx)


class Q3_미카연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10000872], state=1)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10000872], state=0):
            return Q3_영상재생(self.ctx)


class Q3_영상재생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(file_name='MemoryofDragon.swf', movie_id=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_value(type='SceneMovie', name='IsStop') == 1:
            return Q3_시네마틱연출01(self.ctx)


class Q3_시네마틱연출01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='25', seconds=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010005_QD__ACT03__0$', time=4)
        self.set_skip(state=Q3_시네마틱연출02대기)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='25'):
            return Q3_시네마틱연출02대기(self.ctx)


class Q3_시네마틱연출02대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        return Q3_시네마틱연출02(self.ctx)


class Q3_시네마틱연출02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=4001)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        return Q3_시네마틱연출03(self.ctx)


class Q3_시네마틱연출03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='26', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001316, script='$52010005_QD__ACT03__1$', time=3)
        self.set_skip(state=Q3_시네마틱연출04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='26'):
            return Q3_시네마틱연출04(self.ctx)


class Q3_시네마틱연출04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        return Q3_시네마틱연출05(self.ctx)


class Q3_시네마틱연출05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='27', seconds=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='27'):
            return Q3_미카퇴장01(self.ctx)


class Q3_미카퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='30', seconds=2)
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_6013')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='30'):
            return Q3_미카퇴장02(self.ctx)


class Q3_미카퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='31', seconds=3)
        self.set_dialogue(type=2, spawn_id=11001285, script='$52010005_QD__ACT03__2$', time=3)
        self.set_skip(state=Q3_미카퇴장03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='31'):
            return Q3_미카퇴장03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Q3_미카퇴장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawn_id=601, patrol_name='MS2PatrolData_6014')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(box_id=8010, spawn_ids=[601]):
            return Q3_미카퇴장04(self.ctx)


class Q3_미카퇴장04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[601])
        self.set_timer(timer_id='40', seconds=1)
        self.select_camera(trigger_id=4001, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='40'):
            return Q3_업적발생(self.ctx)


class Q3_업적발생(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_achievement(trigger_id=9001, type='trigger', achieve='Intothememory')
        self.destroy_monster(spawn_ids=[501])
        self.spawn_monster(spawn_ids=[502], auto_target=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(box_ids=[9000], quest_ids=[10002823], quest_states=[2]):
            # 3rd Quest
            return Q3_유저퇴장01(self.ctx)


class Q3_유저퇴장01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='41', seconds=2)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='41'):
            return Q3_유저퇴장02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Q3_유저퇴장02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='42', seconds=4)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001316, script='$52010005_QD__ACT03__3$', time=4)
        self.set_skip(state=Q3_유저퇴장03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='42'):
            return Q3_유저퇴장03(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class Q3_유저퇴장03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(map_id=2010026, portal_id=3, box_id=9000)


initial_state = 퀘스트조건03
