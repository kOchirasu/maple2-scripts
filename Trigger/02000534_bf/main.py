""" trigger/02000534_bf/main.xml """
import trigger_api


# 오닉스 타워 3층
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_mesh(trigger_ids=[7000], visible=True)
        self.set_mesh(trigger_ids=[7001], visible=True)
        self.set_mesh(trigger_ids=[7002], visible=True)
        self.set_mesh(trigger_ids=[7003], visible=True)
        self.set_mesh(trigger_ids=[7004], visible=True)
        self.set_mesh(trigger_ids=[7005], visible=True)
        self.set_mesh(trigger_ids=[7006], visible=True)
        self.set_mesh(trigger_ids=[7007], visible=True)
        self.set_mesh(trigger_ids=[7008], visible=True)
        self.set_effect(trigger_ids=[8000])
        self.set_effect(trigger_ids=[8001])
        self.set_effect(trigger_ids=[8002])
        self.set_effect(trigger_ids=[8003])
        self.set_effect(trigger_ids=[8004])
        self.set_effect(trigger_ids=[8005])
        self.set_effect(trigger_ids=[8006])
        self.set_effect(trigger_ids=[8007])
        self.set_effect(trigger_ids=[8008])
        self.set_effect(trigger_ids=[8009])
        self.spawn_monster(spawn_ids=[508,509,510,511])
        self.spawn_monster(spawn_ids=[716,715,713,717,718])
        self.spawn_monster(spawn_ids=[701,702,703,704,705,706,707,708,709,710,711,712])
        self.move_npc(spawn_id=508, patrol_name='MS2PatrolData_4000')
        self.move_npc(spawn_id=509, patrol_name='MS2PatrolData_4001')
        self.move_npc(spawn_id=511, patrol_name='MS2PatrolData_4002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[701], job_code=0):
            return start(self.ctx)


class start(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portal_id=2)
        self.set_event_ui(type=1, arg2='$02000534_BF__MAIN__0$', arg3='3000')
        self.set_portal(portal_id=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 첫번째몬스터전투시작(self.ctx)


class 첫번째몬스터전투시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003132], state=0)
        self.set_interact_object(trigger_ids=[10003133], state=0)
        self.set_interact_object(trigger_ids=[10003134], state=0)
        self.set_interact_object(trigger_ids=[10003135], state=0)
        self.spawn_monster(spawn_ids=[501,520,521,522,523])
        self.add_balloon_talk(spawn_id=523, msg='$02000534_BF__MAIN__1$', duration=3500)
        self.add_balloon_talk(spawn_id=520, msg='$02000534_BF__MAIN__2$', duration=3500)
        self.add_balloon_talk(spawn_id=521, msg='$02000534_BF__MAIN__3$', duration=3500, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[501,520,521,522,523]):
            return 첫번째몬스터처치(self.ctx)


class 첫번째몬스터처치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8000], visible=True)
        self.set_mesh(trigger_ids=[7000])
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__4$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[707], job_code=0):
            return 하렌등장(self.ctx)


class 하렌등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23300001, illust='Haren_smile', duration=4000, script='$02000534_BF__MAIN__5$')
        self.spawn_monster(spawn_ids=[502,524,525,526,527], delay=100)
        self.add_balloon_talk(spawn_id=502, msg='$02000534_BF__MAIN__6$', duration=3500)
        self.add_balloon_talk(spawn_id=527, msg='$02000534_BF__MAIN__7$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 하렌등장2(self.ctx)


class 하렌등장2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23300001, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__8$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 하렌등장3(self.ctx)


class 하렌등장3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23300001, illust='Haren_smile', duration=4000, script='$02000534_BF__MAIN__9$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[502,524,525,526,527]):
            return 두번째몬스터처치(self.ctx)


class 두번째몬스터처치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8005], visible=True)
        self.set_mesh(trigger_ids=[7005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[703], job_code=0):
            return 첫번째연구실몬스터정리(self.ctx)


class 첫번째연구실몬스터정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=713, msg='$02000534_BF__MAIN__10$', duration=3500, delay_tick=2000)
        self.spawn_monster(spawn_ids=[518,519,528], delay=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[518,519,528]):
            return 오브젝트설명1(self.ctx)


class 오브젝트설명1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=713, msg='$02000534_BF__MAIN__11$', duration=3500, delay_tick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 방해1(self.ctx)


class 방해1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$02000534_BF__MAIN__12$', duration=3500, delay_tick=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 첫번째연구실나오기(self.ctx)


class 첫번째연구실나오기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7001])
        self.set_effect(trigger_ids=[8001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[708], job_code=0):
            return 두번째전투판몬스터생성(self.ctx)


class 두번째전투판몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[503,529,530,531,532], delay=500)
        self.add_balloon_talk(spawn_id=503, msg='$02000534_BF__MAIN__13$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[503,529,530,531,532]):
            return 두번째연구소이동(self.ctx)


class 두번째연구소이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[714])
        self.set_effect(trigger_ids=[8006], visible=True)
        self.set_mesh(trigger_ids=[7006])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[704], job_code=0):
            return 두번째연구실몬스터정리(self.ctx)


class 두번째연구실몬스터정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=714, msg='$02000534_BF__MAIN__14$', duration=3500, delay_tick=500)
        self.move_npc(spawn_id=714, patrol_name='MS2PatrolData_4003')
        self.spawn_monster(spawn_ids=[516,517,5516], delay=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[516,517,5516]):
            return 두번째연구실몬스터정리2(self.ctx)


class 두번째연구실몬스터정리2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawn_ids=[714])
        self.set_interact_object(trigger_ids=[10003133], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003133], state=0):
            return 오브젝트설명2(self.ctx)


class 오브젝트설명2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003133], state=0)
        self.add_balloon_talk(msg='$02000534_BF__MAIN__15$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2500):
            return 두번째연구실나오기(self.ctx)


class 두번째연구실나오기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$02000534_BF__MAIN__16$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 세번째전투판(self.ctx)


class 세번째전투판(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7002])
        self.set_effect(trigger_ids=[8002], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[709], job_code=0):
            return 세번째전투판몬스터생성(self.ctx)


class 세번째전투판몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[504,533], delay=500)
        self.add_balloon_talk(spawn_id=504, msg='$02000534_BF__MAIN__17$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[504,533]):
            return 세번째몬스터처치(self.ctx)


class 세번째몬스터처치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8007], visible=True)
        self.set_mesh(trigger_ids=[7007])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[705], job_code=0):
            return 세번째연구소이동(self.ctx)


class 세번째연구소이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[514,515], auto_target=False)
        self.add_balloon_talk(spawn_id=718, msg='$02000534_BF__MAIN__18$', duration=3500)
        self.add_balloon_talk(spawn_id=715, msg='$02000534_BF__MAIN__19$', duration=3500, delay_tick=500)
        self.add_balloon_talk(spawn_id=715, msg='$02000534_BF__MAIN__20$', duration=3500, delay_tick=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[514,515]):
            return 방해3(self.ctx)


class 방해3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=717, msg='$02000534_BF__MAIN__21$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=1000):
            return 방해33(self.ctx)


class 방해33(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(msg='$02000534_BF__MAIN__22$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 네번째전투판(self.ctx)


class 네번째전투판(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7003])
        self.set_effect(trigger_ids=[8003], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[710], job_code=0):
            return 네번째몬스터처치(self.ctx)


class 네번째몬스터처치(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[505,534,535,536,537], auto_target=False)
        self.add_balloon_talk(spawn_id=536, msg='$02000534_BF__MAIN__23$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[505,534,535,536,537]):
            return 네번째연구소로이동(self.ctx)


class 네번째연구소로이동(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8008], visible=True)
        self.set_mesh(trigger_ids=[7008])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[706], job_code=0):
            return 네번째연구소정리(self.ctx)


class 네번째연구소정리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.spawn_monster(spawn_ids=[512,513,5513])
        self.add_balloon_talk(spawn_id=716, msg='$02000534_BF__MAIN__24$', duration=3500, delay_tick=1000)
        self.add_balloon_talk(spawn_id=716, msg='$02000534_BF__MAIN__25$', duration=3500, delay_tick=4500)
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__26$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=4000):
            return 컴퓨터조사하기(self.ctx)


class 컴퓨터조사하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=23300001, illust='Haren_smile', duration=4000, script='$02000534_BF__MAIN__27$')
        self.add_balloon_talk(spawn_id=716, msg='$02000534_BF__MAIN__28$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[512,513,5513]):
            return 번연구실모두정리4(self.ctx)


class 번연구실모두정리4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(trigger_ids=[10003135], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interact_ids=[10003135], state=0):
            return 오브젝트설명4(self.ctx)


class 오브젝트설명4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.add_balloon_talk(msg='$02000534_BF__MAIN__29$', duration=3000)
        self.add_balloon_talk(msg='$02000534_BF__MAIN__30$', duration=3500, delay_tick=3000)
        self.set_scene_skip(state=방해4, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=5500):
            return 방해4(self.ctx)


class 방해4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.remove_balloon_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 방해44(self.ctx)


class 방해44(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__31$')
        self.add_balloon_talk(msg='$02000534_BF__MAIN__32$', duration=3500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=2000):
            return 마지막전투판(self.ctx)


class 마지막전투판(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7004])
        self.set_effect(trigger_ids=[8004], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[702], job_code=0):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[7004], visible=True)
        self.set_portal(portal_id=2)
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=4000, script='$02000534_BF__MAIN__33$')
        self.spawn_monster(spawn_ids=[507])
        self.add_balloon_talk(spawn_id=507, msg='$02000534_BF__MAIN__34$', duration=3500, delay_tick=1500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_hp(spawn_id=507, is_relative=True) <= 50:
            return 업그레이드시작(self.ctx)
        if self.monster_dead(spawn_ids=[507]):
            return 포탈생성(self.ctx)


class 업그레이드시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=15, interval=1)
        self.spawn_monster(spawn_ids=[9901,9902,9903,9904], auto_target=False)
        self.add_balloon_talk(spawn_id=507, msg='$02000534_BF__MAIN__35$', duration=3500, delay_tick=500)
        self.set_event_ui(type=1, arg2='$02000534_BF__MAIN__36$', arg3='3000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=15000):
            return 업그레이드성공체크(self.ctx)


class 업그레이드성공체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=100):
            return 자폭스킬(self.ctx)
        if self.monster_dead(spawn_ids=[9901,9902,9903,9904]):
            return 실패(self.ctx)
        if self.monster_dead(spawn_ids=[507]):
            return 포탈생성(self.ctx)


class 자폭스킬(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=507, msg='$02000534_BF__MAIN__37$', duration=3500, delay_tick=500)
        self.set_ai_extra_data(key='bomb', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[507]):
            return 포탈생성(self.ctx)


class 실패(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawn_id=507, msg='$02000534_BF__MAIN__38$', duration=3500, delay_tick=500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[507]):
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timer_id='1', seconds=15)
        self.side_npc_talk(npc_id=11004639, illust='Jay_normal', duration=3000, script='$02000534_BF__MAIN__39$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(wait_tick=3000):
            return 포탈생성2(self.ctx)


class 포탈생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$02000534_BF__MAIN__40$', arg3='3000')
        self.set_portal(portal_id=2, visible=True, enable=True, minimap_visible=True)


initial_state = idle
