""" trigger/02020112_bf/jumproom.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.enable_spawn_point_pc(spawn_id=1)
        self.set_effect(trigger_ids=[8005])
        self.set_effect(trigger_ids=[8006])
        self.set_effect(trigger_ids=[8007])
        self.set_effect(trigger_ids=[8008])
        self.set_user_value(trigger_id=99990009, key='ButtonSuccess', value=0)
        self.set_user_value(trigger_id=99990010, key='ButtonSuccess', value=0)
        self.set_user_value(trigger_id=99990011, key='ButtonSuccess', value=0)
        self.set_user_value(trigger_id=99990012, key='ButtonSuccess', value=0)
        self.set_user_value(trigger_id=99990001, key='MonsterDead', value=0)
        self.set_actor(trigger_id=9905, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9906, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9907, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')
        self.set_actor(trigger_id=9908, visible=True, initial_sequence='Interaction_Lapentafoothold_A01_Off')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=931) >= 4:
            # <4명 이상 입장시 활성화>
            return 감지(self.ctx)
        if self.user_detected(box_ids=[931], job_code=0):
            return 감지(self.ctx)


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[8005], visible=True)
        self.set_effect(trigger_ids=[8006], visible=True)
        self.set_effect(trigger_ids=[8007], visible=True)
        self.set_effect(trigger_ids=[8008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[921], job_code=0) and self.user_detected(box_ids=[922], job_code=0) and self.user_detected(box_ids=[923], job_code=0) and self.user_detected(box_ids=[924], job_code=0):
            return 성공(self.ctx)


class 성공(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # <재접속 유저를 위해 버프 지속적으로 쏴주기 캔슬>
        self.set_user_value(trigger_id=99990021, key='Reconnect', value=2)
        self.set_event_ui(type=1, arg2='$02020112_BF__JUMPROOM__0$', arg3='5000')
        self.set_gravity(gravity=0.0)
        self.set_effect(trigger_ids=[8005])
        self.set_effect(trigger_ids=[8006])
        self.set_effect(trigger_ids=[8007])
        self.set_effect(trigger_ids=[8008])
        self.add_buff(box_ids=[931], skill_id=70002112, level=1, is_skill_set=False)
        self.set_user_value(trigger_id=99990009, key='ButtonSuccess', value=1)
        self.set_user_value(trigger_id=99990010, key='ButtonSuccess', value=1)
        self.set_user_value(trigger_id=99990011, key='ButtonSuccess', value=1)
        self.set_user_value(trigger_id=99990012, key='ButtonSuccess', value=1)
        self.set_mesh(trigger_ids=[1501,1502,1503,1504,1505,1506,1507,1508,1509], interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1510,1511,1512,1513,1514,1515,1516,1517,1518], interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1519,1520,1521,1522,1523,1524,1525,1526,1527], interval=20, fade=3.0)
        self.set_mesh(trigger_ids=[1528,1529,1530,1531,1532,1533,1534,1535,1536], interval=20, fade=3.0)
        self.set_actor(trigger_id=9905, initial_sequence='Interaction_Lapentafoothold_A01_On')
        self.set_actor(trigger_id=9906, initial_sequence='Interaction_Lapentafoothold_A01_On')
        self.set_actor(trigger_id=9907, initial_sequence='Interaction_Lapentafoothold_A01_On')
        self.set_actor(trigger_id=9908, initial_sequence='Interaction_Lapentafoothold_A01_On')
        self.spawn_monster(spawn_ids=[152,153,154,155], auto_target=False)
        self.enable_spawn_point_pc(spawn_id=0)
        self.enable_spawn_point_pc(spawn_id=1, is_enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(spawn_ids=[152,153,154,155]):
            self.set_user_value(trigger_id=99990001, key='MonsterDead', value=1) # <점프방 몬스터 체크>


initial_state = 대기
