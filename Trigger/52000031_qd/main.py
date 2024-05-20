""" trigger/52000031_qd/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100,3200], visible=True)
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115])
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212])
        self.set_effect(trigger_ids=[601])
        self.set_effect(trigger_ids=[602])
        self.set_effect(trigger_ids=[603])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[101], job_code=90):
            return 연출시작(self.ctx)
        if self.user_detected(box_ids=[101], job_code=10):
            return 연출시작10(self.ctx)
        if self.user_detected(box_ids=[101], job_code=1):
            return 연출시작10(self.ctx)
        if self.user_detected(box_ids=[101], job_code=20):
            return 연출시작20(self.ctx)
        if self.user_detected(box_ids=[101], job_code=30):
            return 연출시작30(self.ctx)
        if self.user_detected(box_ids=[101], job_code=40):
            return 연출시작40(self.ctx)
        if self.user_detected(box_ids=[101], job_code=50):
            return 연출시작50(self.ctx)
        if self.user_detected(box_ids=[101], job_code=60):
            return 연출시작60(self.ctx)
        if self.user_detected(box_ids=[101], job_code=70):
            return 연출시작50(self.ctx)
        if self.user_detected(box_ids=[101], job_code=80):
            return 연출시작60(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000031_QD__MAIN__0$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출시작10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000076, script='$52000031_QD__MAIN__1$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출시작20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001581, script='$52000031_QD__MAIN__2$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출시작30(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_effect(trigger_ids=[602], visible=True)
        self.set_dialogue(type=2, spawn_id=11000032, script='$52000031_QD__MAIN__3$', time=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출시작40(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001578, script='$52000031_QD__MAIN__4$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출시작50(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11000015, script='$52000031_QD__MAIN__5$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출시작60(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001583, script='$52000031_QD__MAIN__6$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출시작70(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001586, script='$52000031_QD__MAIN__7$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 연출시작80(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301)
        self.spawn_monster(spawn_ids=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,2001,2002])
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001584, script='$52000031_QD__MAIN__8$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 전투시작(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(trigger_id=301, enable=False)
        self.select_camera(trigger_id=302)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2001]):
            return 차전투2(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[2002])


class 차전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[2003,2004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[2003]):
            return 렌듀비앙대사02(self.ctx)

    def on_exit(self) -> None:
        self.destroy_monster(spawn_ids=[2004])
        self.select_camera(trigger_id=302, enable=False)


class 렌듀비앙대사02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[3100,3200])
        self.set_mesh(trigger_ids=[3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113,3114,3115], visible=True, interval=100, fade=1.0)
        self.set_mesh(trigger_ids=[3201,3202,3203,3204,3205,3206,3207,3208,3209,3210,3211,3212], visible=True, interval=100, fade=1.0)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_dialogue(type=2, spawn_id=11001230, script='$52000031_QD__MAIN__9$', time=3)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000031_QD__MAIN__10$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=6000):
            return 유페리아대사_기타음성1(self.ctx)


class 유페리아대사_기타음성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[603], visible=True)
        self.set_dialogue(type=2, spawn_id=11001564, script='$52000031_QD__MAIN__11$', time=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3500):
            return 이슈라외침01(self.ctx)


class 이슈라외침01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[601], visible=True)
        self.set_dialogue(type=2, spawn_id=11001244, script='$52000031_QD__MAIN__12$', time=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            self.move_user(map_id=52000032)
            return 종료(self.ctx)

    def on_exit(self) -> None:
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
