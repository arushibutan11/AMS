PGDMP     	    6    	            u            traffic    9.6.3    9.6.3 �    g
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            h
           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            i
           1262    16394    traffic    DATABASE     e   CREATE DATABASE traffic WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C' LC_CTYPE = 'C';
    DROP DATABASE traffic;
             root    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            j
           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12655    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            k
           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    16395 
   auth_group    TABLE     ^   CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);
    DROP TABLE public.auth_group;
       public         root    false    3            �            1259    16398    auth_group_id_seq    SEQUENCE     s   CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       root    false    3    185            l
           0    0    auth_group_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;
            public       root    false    186            �            1259    16400    auth_group_permissions    TABLE     �   CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         root    false    3            �            1259    16403    auth_group_permissions_id_seq    SEQUENCE        CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       root    false    187    3            m
           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;
            public       root    false    188            �            1259    16405    auth_permission    TABLE     �   CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         root    false    3            �            1259    16408    auth_permission_id_seq    SEQUENCE     x   CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       root    false    3    189            n
           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;
            public       root    false    190            �            1259    16410 	   auth_user    TABLE     �  CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         root    false    3            �            1259    16416    auth_user_groups    TABLE     x   CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         root    false    3            �            1259    16419    auth_user_groups_id_seq    SEQUENCE     y   CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       root    false    3    192            o
           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;
            public       root    false    193            �            1259    16421    auth_user_id_seq    SEQUENCE     r   CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       root    false    3    191            p
           0    0    auth_user_id_seq    SEQUENCE OWNED BY     7   ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;
            public       root    false    194            �            1259    16423    auth_user_user_permissions    TABLE     �   CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         root    false    3            �            1259    16426 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       root    false    195    3            q
           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;
            public       root    false    196            �            1259    16428    django_admin_log    TABLE     �  CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         root    false    3            �            1259    16435    django_admin_log_id_seq    SEQUENCE     y   CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       root    false    197    3            r
           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;
            public       root    false    198            �            1259    16437    django_content_type    TABLE     �   CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         root    false    3            �            1259    16440    django_content_type_id_seq    SEQUENCE     |   CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       root    false    199    3            s
           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;
            public       root    false    200            �            1259    16442    django_migrations    TABLE     �   CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         root    false    3            �            1259    16448    django_migrations_id_seq    SEQUENCE     z   CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       root    false    201    3            t
           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;
            public       root    false    202            �            1259    16450    django_session    TABLE     �   CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         root    false    3            �            1259    16456    fir_circles    TABLE     +  CREATE TABLE fir_circles (
    "DISTNAM" character varying(50) NOT NULL,
    "DIST" character varying(4) NOT NULL,
    "CIRCLE" character varying(4) NOT NULL,
    "CIRCLENAM" character varying(50) NOT NULL,
    "RANGE" character varying(4) NOT NULL,
    "RANGENAM" character varying(50) NOT NULL
);
    DROP TABLE public.fir_circles;
       public         root    false    3            �            1259    16459    fir_details    TABLE     �  CREATE TABLE fir_details (
    "ACC_ID" character varying(15) NOT NULL,
    "RNG" character varying(5) NOT NULL,
    "CIRCLE_id" character varying(4) NOT NULL,
    "DIST" character varying(5) NOT NULL,
    "PS_id" character varying(50) NOT NULL,
    "FIRNO" integer NOT NULL,
    "SECTION_id" integer NOT NULL,
    "TIME_OCC" time without time zone NOT NULL,
    "TIME_TYPE" character varying(15) NOT NULL,
    "DATE_OCC" date NOT NULL,
    "PLACE_OCC" character varying(140) NOT NULL,
    "ROAD_id" character varying(50) NOT NULL,
    "ROADNAME" character varying(150) NOT NULL,
    "LOCATION" character varying(140) NOT NULL,
    "CATEGORY" character varying(140) NOT NULL,
    "VEHTYPE1_id" character varying(20) NOT NULL,
    "TWW1" character varying(15) NOT NULL,
    "RNOV1A" character varying(15) NOT NULL,
    "RNOV1B" character varying(10) NOT NULL,
    "VEHTYPE2_id" character varying(30) NOT NULL,
    "TWW2" character varying(15) NOT NULL,
    "RNOV2A" character varying(10) NOT NULL,
    "RNOV2B" character varying(4) NOT NULL,
    "SELF_TYPE_id" character varying(20) NOT NULL,
    "INJURED" integer NOT NULL,
    "INJMALE" integer NOT NULL,
    "INJFEMALE" integer NOT NULL,
    "INJBOY" integer NOT NULL,
    "INJGIRL" integer NOT NULL,
    "KILLED" integer NOT NULL,
    "KILMALE" integer NOT NULL,
    "KILFEMALE" integer NOT NULL,
    "KILBOY" integer NOT NULL,
    "KILGIRL" integer NOT NULL,
    "PEDESTRIAN" integer NOT NULL,
    "ACCTYPE" character varying(20) NOT NULL,
    "ACCID_TYPE" character varying(100) NOT NULL,
    "VICTIM" character varying(100) NOT NULL,
    "DUPL" character varying(15) NOT NULL,
    "PENDING" character varying(15) NOT NULL,
    "DAY_NIGHT" character varying(15) NOT NULL,
    "YEAR" integer NOT NULL,
    "TIME_SLOT" character varying(15) NOT NULL,
    "MONTH" character varying(15) NOT NULL,
    "FN" character varying(15) NOT NULL,
    "ACCAGE" character varying(15) NOT NULL,
    "ACCSEX" character varying(15) NOT NULL,
    "ACCDRUNK" boolean NOT NULL,
    "Intersection" character varying(150) NOT NULL,
    routeno character varying(15),
    case_status character varying(15) NOT NULL,
    convert_case character varying(15) NOT NULL,
    "BRIEF_FACTS" character varying(500) NOT NULL,
    dri_lic_no character varying(150) NOT NULL,
    dri_name character varying(150) NOT NULL,
    dri_fath character varying(150) NOT NULL,
    dri_sex character varying(15) NOT NULL,
    dri_age integer NOT NULL,
    dri_add character varying(150) NOT NULL,
    dri_arrest character varying(15) NOT NULL,
    dri_place character varying(150) NOT NULL,
    dri_lic_date_issu date NOT NULL,
    dri_lic_date_upto date NOT NULL,
    dri_lic_status character varying(15) NOT NULL,
    "REMARK" character varying(300) NOT NULL,
    "CONFIRM" character varying(15) NOT NULL,
    "LONGITUDE" character varying(15) NOT NULL,
    "LATITUDE" character varying(15) NOT NULL,
    "CONVERT" character varying(15) NOT NULL,
    "CONVERT_DATE" date NOT NULL,
    "CN_DT" character varying(150) NOT NULL,
    "CONVERT_FN" character varying(150) NOT NULL,
    "BUS_NO" character varying(15) NOT NULL,
    "BLACK_SPOT" character varying(15) NOT NULL,
    "BLACK_SPOT_NO" character varying(15) NOT NULL,
    "FOR_BLK" character varying(15) NOT NULL,
    "STATUS" character varying(15) NOT NULL,
    "F_STATUS" character varying(15) NOT NULL,
    dri_add1 character varying(15) NOT NULL,
    "RIDER_HELMET" character varying(15) NOT NULL,
    "PILLION_HELMET" character varying(15) NOT NULL,
    "STATE" character varying(15) NOT NULL,
    "SCANNED" character varying(15) NOT NULL,
    "HIT_AND_RUN_UPDATE1" character varying(15) NOT NULL,
    CONSTRAINT "fir_details_INJBOY_check" CHECK (("INJBOY" >= 0)),
    CONSTRAINT "fir_details_INJFEMALE_check" CHECK (("INJFEMALE" >= 0)),
    CONSTRAINT "fir_details_INJGIRL_check" CHECK (("INJGIRL" >= 0)),
    CONSTRAINT "fir_details_INJMALE_check" CHECK (("INJMALE" >= 0)),
    CONSTRAINT "fir_details_INJURED_check" CHECK (("INJURED" >= 0)),
    CONSTRAINT "fir_details_KILBOY_check" CHECK (("KILBOY" >= 0)),
    CONSTRAINT "fir_details_KILFEMALE_check" CHECK (("KILFEMALE" >= 0)),
    CONSTRAINT "fir_details_KILGIRL_check" CHECK (("KILGIRL" >= 0)),
    CONSTRAINT "fir_details_KILLED_check" CHECK (("KILLED" >= 0)),
    CONSTRAINT "fir_details_KILMALE_check" CHECK (("KILMALE" >= 0)),
    CONSTRAINT "fir_details_PEDESTRIAN_check" CHECK (("PEDESTRIAN" >= 0)),
    CONSTRAINT "fir_details_YEAR_check" CHECK (("YEAR" >= 0)),
    CONSTRAINT fir_details_dri_age_6d7e126d_check CHECK ((dri_age >= 0))
);
    DROP TABLE public.fir_details;
       public         root    false    3            �            1259    16644    fir_injured    TABLE     �  CREATE TABLE fir_injured (
    id integer NOT NULL,
    "PS" character varying(5) NOT NULL,
    "FIRNO" integer NOT NULL,
    "YEAR" integer NOT NULL,
    "INJSEX" character varying(15) NOT NULL,
    "INJAGE" character varying(15) NOT NULL,
    "INJTYPE" character varying(5) NOT NULL,
    "ACCID_ID_id" character varying(15) NOT NULL,
    CONSTRAINT "fir_injured_YEAR_check" CHECK (("YEAR" >= 0))
);
    DROP TABLE public.fir_injured;
       public         root    false    3            �            1259    16642    fir_injured_id_seq    SEQUENCE     t   CREATE SEQUENCE fir_injured_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.fir_injured_id_seq;
       public       root    false    210    3            u
           0    0    fir_injured_id_seq    SEQUENCE OWNED BY     ;   ALTER SEQUENCE fir_injured_id_seq OWNED BY fir_injured.id;
            public       root    false    209            �            1259    16654 
   fir_killed    TABLE     �  CREATE TABLE fir_killed (
    id integer NOT NULL,
    "PS" character varying(5) NOT NULL,
    "FIRNO" integer NOT NULL,
    "YEAR" integer NOT NULL,
    "SEX" character varying(15) NOT NULL,
    "AGE" character varying(15) NOT NULL,
    "TYPE" character varying(20) NOT NULL,
    "ACCID_ID_id" character varying(15) NOT NULL,
    CONSTRAINT "fir_killed_YEAR_check" CHECK (("YEAR" >= 0))
);
    DROP TABLE public.fir_killed;
       public         root    false    3            �            1259    16652    fir_killed_id_seq    SEQUENCE     s   CREATE SEQUENCE fir_killed_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.fir_killed_id_seq;
       public       root    false    212    3            v
           0    0    fir_killed_id_seq    SEQUENCE OWNED BY     9   ALTER SEQUENCE fir_killed_id_seq OWNED BY fir_killed.id;
            public       root    false    211            �            1259    16477    fir_policestation    TABLE     �  CREATE TABLE fir_policestation (
    "DISTNAM" character varying(50) NOT NULL,
    "DIST" character varying(20) NOT NULL,
    "CIRCLENAM" character varying(50) NOT NULL,
    "RANGE" character varying(4) NOT NULL,
    "RANGENAM" character varying(50) NOT NULL,
    "PS" character varying(20) NOT NULL,
    "PSNAME" character varying(100) NOT NULL,
    "CIRCLE_PS" character varying(50) NOT NULL,
    "CIRCLE_id" character varying(4) NOT NULL
);
 %   DROP TABLE public.fir_policestation;
       public         root    false    3            �            1259    16480 	   fir_roads    TABLE     �  CREATE TABLE fir_roads (
    "RNG" character varying(5) NOT NULL,
    "DIST" character varying(5) NOT NULL,
    "ROADNAME" character varying(50) NOT NULL,
    "ROAD" integer NOT NULL,
    "PS" character varying(5) NOT NULL,
    "PLACE_OCC" character varying(50) NOT NULL,
    "NEW" character varying(50) NOT NULL,
    "PSNAME" character varying(50) NOT NULL,
    "NEW1" character varying(50) NOT NULL,
    "CIRCLE_id" character varying(4) NOT NULL
);
    DROP TABLE public.fir_roads;
       public         root    false    3            �            1259    16483    fir_sections    TABLE     �   CREATE TABLE fir_sections (
    "SECTION" integer NOT NULL,
    "SECTIONDTL" character varying(50) NOT NULL,
    "ACCTYPE" character varying(5) NOT NULL,
    "ACCTYPEN" character varying(25) NOT NULL
);
     DROP TABLE public.fir_sections;
       public         root    false    3            �            1259    17609    fir_self_type    TABLE     �   CREATE TABLE fir_self_type (
    "SNO" character varying(100) NOT NULL,
    "CODE" character varying(20) NOT NULL,
    "TYPE" character varying(100) NOT NULL
);
 !   DROP TABLE public.fir_self_type;
       public         root    false    3            �            1259    16757    fir_vehtype1    TABLE     F
  CREATE TABLE fir_vehtype1 (
    "VEHTYPE" character varying(20) NOT NULL,
    "VEHDETL" character varying(20) NOT NULL,
    "VEHDTL" character varying(40) NOT NULL,
    "SIMPLE" character varying(10),
    "NONINJ" character varying(10),
    "FATAL" character varying(10),
    "PERINJ" character varying(10),
    "PERKIL" character varying(10),
    "PEDESTRIAN" character varying(10),
    "CARI" character varying(10),
    "CARK" character varying(10),
    "DTCI" character varying(10),
    "DTCK" character varying(10),
    "BLBI" character varying(10),
    "BLBK" character varying(10),
    "BUSI" character varying(10),
    "BUSK" character varying(10),
    "OSBI" character varying(10),
    "OSBK" character varying(10),
    "MBSI" character varying(10),
    "MBSK" character varying(10),
    "TAXI" character varying(10),
    "TAXK" character varying(10),
    "TSRK" character varying(10),
    "TSRI" character varying(10),
    "TWWI" character varying(10),
    "TWWK" character varying(10),
    "MILI" character varying(10),
    "MILK" character varying(10),
    "DLVI" character varying(10),
    "DLVK" character varying(10),
    "TRCI" character varying(10),
    "TRCK" character varying(10),
    "POVI" character varying(10),
    "POVK" character varying(10),
    "AMBI" character varying(10),
    "AMBK" character varying(10),
    "STRI" character varying(10),
    "STRK" character varying(10),
    "TMPI" character varying(10),
    "TMPK" character varying(10),
    "MATI" character varying(10),
    "MATK" character varying(10),
    "TNKI" character varying(10),
    "TNKK" character varying(10),
    "UNKI" character varying(10),
    "UNKK" character varying(10),
    "CYCI" character varying(10),
    "CYCK" character varying(10),
    "TNGI" character varying(10),
    "TNGK" character varying(10),
    "CYRI" character varying(10),
    "CYRK" character varying(10),
    "HDCI" character varying(10),
    "HDCK" character varying(10),
    "BULI" character varying(10),
    "BULK" character varying(10),
    "ANII" character varying(10),
    "ANIK" character varying(10),
    "CRNI" character varying(10),
    "CRNK" character varying(10),
    "UDTI" character varying(10),
    "UDTK" character varying(10),
    "PEDI" character varying(10),
    "PEDK" character varying(10),
    "HTVI" character varying(10),
    "HTVK" character varying(10),
    "SLFI" character varying(10),
    "SLFK" character varying(10),
    "ELTI" character varying(10),
    "ELTK" character varying(10),
    "WLLI" character varying(10),
    "WLLK" character varying(10),
    "PASI" character varying(10),
    "PASK" character varying(10)
);
     DROP TABLE public.fir_vehtype1;
       public         root    false    3            �            1259    17583    fir_vehtype2    TABLE     F
  CREATE TABLE fir_vehtype2 (
    "VEHTYPE" character varying(30) NOT NULL,
    "VEHDETL" character varying(20) NOT NULL,
    "VEHDTL" character varying(40) NOT NULL,
    "SIMPLE" character varying(10),
    "NONINJ" character varying(10),
    "FATAL" character varying(10),
    "PERINJ" character varying(10),
    "PERKIL" character varying(10),
    "PEDESTRIAN" character varying(10),
    "CARI" character varying(10),
    "CARK" character varying(10),
    "DTCI" character varying(10),
    "DTCK" character varying(10),
    "BLBI" character varying(10),
    "BLBK" character varying(10),
    "BUSI" character varying(10),
    "BUSK" character varying(10),
    "OSBI" character varying(10),
    "OSBK" character varying(10),
    "MBSI" character varying(10),
    "MBSK" character varying(10),
    "TAXI" character varying(10),
    "TAXK" character varying(10),
    "TSRI" character varying(10),
    "TSRK" character varying(10),
    "TWWI" character varying(10),
    "TWWK" character varying(10),
    "MILI" character varying(10),
    "MILK" character varying(10),
    "DLVI" character varying(10),
    "DLVK" character varying(10),
    "TRCI" character varying(10),
    "TRCK" character varying(10),
    "POVI" character varying(10),
    "POVK" character varying(10),
    "AMBI" character varying(10),
    "AMBK" character varying(10),
    "STRI" character varying(10),
    "STRK" character varying(10),
    "TMPI" character varying(10),
    "TMPK" character varying(10),
    "CYCI" character varying(10),
    "CYRI" character varying(10),
    "CYRK" character varying(10),
    "HDCI" character varying(10),
    "HDCK" character varying(10),
    "BULI" character varying(10),
    "BULK" character varying(10),
    "ANII" character varying(10),
    "ANIK" character varying(10),
    "CRNI" character varying(10),
    "CRNK" character varying(10),
    "UDTI" character varying(10),
    "UDTK" character varying(10),
    "PEDI" character varying(10),
    "PEDK" character varying(10),
    "HTVI" character varying(10),
    "HTVK" character varying(10),
    "SLFI" character varying(10),
    "SLFK" character varying(10),
    "ELTI" character varying(10),
    "ELTK" character varying(10),
    "WLLI" character varying(10),
    "WLLK" character varying(10),
    "PASI" character varying(10),
    "PASK" character varying(10),
    "CYCK" character varying(10),
    "MATI" character varying(10),
    "MATK" character varying(10),
    "TNGI" character varying(10),
    "TNGK" character varying(10),
    "TNKI" character varying(10),
    "TNKK" character varying(10),
    "UNKI" character varying(10),
    "UNKK" character varying(10)
);
     DROP TABLE public.fir_vehtype2;
       public         root    false    3            B	           2604    16486    auth_group id    DEFAULT     `   ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       root    false    186    185            C	           2604    16487    auth_group_permissions id    DEFAULT     x   ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       root    false    188    187            D	           2604    16488    auth_permission id    DEFAULT     j   ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       root    false    190    189            E	           2604    16489    auth_user id    DEFAULT     ^   ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       root    false    194    191            F	           2604    16490    auth_user_groups id    DEFAULT     l   ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       root    false    193    192            G	           2604    16491    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       root    false    196    195            H	           2604    16492    django_admin_log id    DEFAULT     l   ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       root    false    198    197            J	           2604    16493    django_content_type id    DEFAULT     r   ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       root    false    200    199            K	           2604    16494    django_migrations id    DEFAULT     n   ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       root    false    202    201            Y	           2604    16647    fir_injured id    DEFAULT     b   ALTER TABLE ONLY fir_injured ALTER COLUMN id SET DEFAULT nextval('fir_injured_id_seq'::regclass);
 =   ALTER TABLE public.fir_injured ALTER COLUMN id DROP DEFAULT;
       public       root    false    210    209    210            [	           2604    16657    fir_killed id    DEFAULT     `   ALTER TABLE ONLY fir_killed ALTER COLUMN id SET DEFAULT nextval('fir_killed_id_seq'::regclass);
 <   ALTER TABLE public.fir_killed ALTER COLUMN id DROP DEFAULT;
       public       root    false    211    212    212            F
          0    16395 
   auth_group 
   TABLE DATA               '   COPY auth_group (id, name) FROM stdin;
    public       root    false    185   �      w
           0    0    auth_group_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('auth_group_id_seq', 1, false);
            public       root    false    186            H
          0    16400    auth_group_permissions 
   TABLE DATA               F   COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       root    false    187          x
           0    0    auth_group_permissions_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);
            public       root    false    188            J
          0    16405    auth_permission 
   TABLE DATA               G   COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       root    false    189         y
           0    0    auth_permission_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('auth_permission_id_seq', 48, true);
            public       root    false    190            L
          0    16410 	   auth_user 
   TABLE DATA               �   COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public       root    false    191          M
          0    16416    auth_user_groups 
   TABLE DATA               :   COPY auth_user_groups (id, user_id, group_id) FROM stdin;
    public       root    false    192   8      z
           0    0    auth_user_groups_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);
            public       root    false    193            {
           0    0    auth_user_id_seq    SEQUENCE SET     7   SELECT pg_catalog.setval('auth_user_id_seq', 2, true);
            public       root    false    194            P
          0    16423    auth_user_user_permissions 
   TABLE DATA               I   COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       root    false    195   U      |
           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);
            public       root    false    196            R
          0    16428    django_admin_log 
   TABLE DATA               �   COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       root    false    197   r      }
           0    0    django_admin_log_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);
            public       root    false    198            T
          0    16437    django_content_type 
   TABLE DATA               <   COPY django_content_type (id, app_label, model) FROM stdin;
    public       root    false    199   �      ~
           0    0    django_content_type_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('django_content_type_id_seq', 16, true);
            public       root    false    200            V
          0    16442    django_migrations 
   TABLE DATA               <   COPY django_migrations (id, app, name, applied) FROM stdin;
    public       root    false    201   B      
           0    0    django_migrations_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('django_migrations_id_seq', 41, true);
            public       root    false    202            X
          0    16450    django_session 
   TABLE DATA               I   COPY django_session (session_key, session_data, expire_date) FROM stdin;
    public       root    false    203   W      Y
          0    16456    fir_circles 
   TABLE DATA               ]   COPY fir_circles ("DISTNAM", "DIST", "CIRCLE", "CIRCLENAM", "RANGE", "RANGENAM") FROM stdin;
    public       root    false    204   �      Z
          0    16459    fir_details 
   TABLE DATA               �  COPY fir_details ("ACC_ID", "RNG", "CIRCLE_id", "DIST", "PS_id", "FIRNO", "SECTION_id", "TIME_OCC", "TIME_TYPE", "DATE_OCC", "PLACE_OCC", "ROAD_id", "ROADNAME", "LOCATION", "CATEGORY", "VEHTYPE1_id", "TWW1", "RNOV1A", "RNOV1B", "VEHTYPE2_id", "TWW2", "RNOV2A", "RNOV2B", "SELF_TYPE_id", "INJURED", "INJMALE", "INJFEMALE", "INJBOY", "INJGIRL", "KILLED", "KILMALE", "KILFEMALE", "KILBOY", "KILGIRL", "PEDESTRIAN", "ACCTYPE", "ACCID_TYPE", "VICTIM", "DUPL", "PENDING", "DAY_NIGHT", "YEAR", "TIME_SLOT", "MONTH", "FN", "ACCAGE", "ACCSEX", "ACCDRUNK", "Intersection", routeno, case_status, convert_case, "BRIEF_FACTS", dri_lic_no, dri_name, dri_fath, dri_sex, dri_age, dri_add, dri_arrest, dri_place, dri_lic_date_issu, dri_lic_date_upto, dri_lic_status, "REMARK", "CONFIRM", "LONGITUDE", "LATITUDE", "CONVERT", "CONVERT_DATE", "CN_DT", "CONVERT_FN", "BUS_NO", "BLACK_SPOT", "BLACK_SPOT_NO", "FOR_BLK", "STATUS", "F_STATUS", dri_add1, "RIDER_HELMET", "PILLION_HELMET", "STATE", "SCANNED", "HIT_AND_RUN_UPDATE1") FROM stdin;
    public       root    false    205   �      _
          0    16644    fir_injured 
   TABLE DATA               g   COPY fir_injured (id, "PS", "FIRNO", "YEAR", "INJSEX", "INJAGE", "INJTYPE", "ACCID_ID_id") FROM stdin;
    public       root    false    210   �      �
           0    0    fir_injured_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('fir_injured_id_seq', 1, false);
            public       root    false    209            a
          0    16654 
   fir_killed 
   TABLE DATA               ]   COPY fir_killed (id, "PS", "FIRNO", "YEAR", "SEX", "AGE", "TYPE", "ACCID_ID_id") FROM stdin;
    public       root    false    212         �
           0    0    fir_killed_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('fir_killed_id_seq', 1, false);
            public       root    false    211            [
          0    16477    fir_policestation 
   TABLE DATA               �   COPY fir_policestation ("DISTNAM", "DIST", "CIRCLENAM", "RANGE", "RANGENAM", "PS", "PSNAME", "CIRCLE_PS", "CIRCLE_id") FROM stdin;
    public       root    false    206   ,      \
          0    16480 	   fir_roads 
   TABLE DATA               x   COPY fir_roads ("RNG", "DIST", "ROADNAME", "ROAD", "PS", "PLACE_OCC", "NEW", "PSNAME", "NEW1", "CIRCLE_id") FROM stdin;
    public       root    false    207   .      ]
          0    16483    fir_sections 
   TABLE DATA               O   COPY fir_sections ("SECTION", "SECTIONDTL", "ACCTYPE", "ACCTYPEN") FROM stdin;
    public       root    false    208   �d      d
          0    17609    fir_self_type 
   TABLE DATA               7   COPY fir_self_type ("SNO", "CODE", "TYPE") FROM stdin;
    public       root    false    215   e      b
          0    16757    fir_vehtype1 
   TABLE DATA               �  COPY fir_vehtype1 ("VEHTYPE", "VEHDETL", "VEHDTL", "SIMPLE", "NONINJ", "FATAL", "PERINJ", "PERKIL", "PEDESTRIAN", "CARI", "CARK", "DTCI", "DTCK", "BLBI", "BLBK", "BUSI", "BUSK", "OSBI", "OSBK", "MBSI", "MBSK", "TAXI", "TAXK", "TSRK", "TSRI", "TWWI", "TWWK", "MILI", "MILK", "DLVI", "DLVK", "TRCI", "TRCK", "POVI", "POVK", "AMBI", "AMBK", "STRI", "STRK", "TMPI", "TMPK", "MATI", "MATK", "TNKI", "TNKK", "UNKI", "UNKK", "CYCI", "CYCK", "TNGI", "TNGK", "CYRI", "CYRK", "HDCI", "HDCK", "BULI", "BULK", "ANII", "ANIK", "CRNI", "CRNK", "UDTI", "UDTK", "PEDI", "PEDK", "HTVI", "HTVK", "SLFI", "SLFK", "ELTI", "ELTK", "WLLI", "WLLK", "PASI", "PASK") FROM stdin;
    public       root    false    213   �f      c
          0    17583    fir_vehtype2 
   TABLE DATA               �  COPY fir_vehtype2 ("VEHTYPE", "VEHDETL", "VEHDTL", "SIMPLE", "NONINJ", "FATAL", "PERINJ", "PERKIL", "PEDESTRIAN", "CARI", "CARK", "DTCI", "DTCK", "BLBI", "BLBK", "BUSI", "BUSK", "OSBI", "OSBK", "MBSI", "MBSK", "TAXI", "TAXK", "TSRI", "TSRK", "TWWI", "TWWK", "MILI", "MILK", "DLVI", "DLVK", "TRCI", "TRCK", "POVI", "POVK", "AMBI", "AMBK", "STRI", "STRK", "TMPI", "TMPK", "CYCI", "CYRI", "CYRK", "HDCI", "HDCK", "BULI", "BULK", "ANII", "ANIK", "CRNI", "CRNK", "UDTI", "UDTK", "PEDI", "PEDK", "HTVI", "HTVK", "SLFI", "SLFK", "ELTI", "ELTK", "WLLI", "WLLK", "PASI", "PASK", "CYCK", "MATI", "MATK", "TNGI", "TNGK", "TNKI", "TNKK", "UNKI", "UNKK") FROM stdin;
    public       root    false    214   �k      _	           2606    16496    auth_group auth_group_name_key 
   CONSTRAINT     R   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         root    false    185    185            d	           2606    16498 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public         root    false    187    187    187            g	           2606    16500 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         root    false    187    187            a	           2606    16502    auth_group auth_group_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         root    false    185    185            j	           2606    16504 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public         root    false    189    189    189            l	           2606    16506 $   auth_permission auth_permission_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         root    false    189    189            t	           2606    16508 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         root    false    192    192            w	           2606    16510 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public         root    false    192    192    192            n	           2606    16512    auth_user auth_user_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         root    false    191    191            z	           2606    16514 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         root    false    195    195            }	           2606    16516 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public         root    false    195    195    195            q	           2606    16518     auth_user auth_user_username_key 
   CONSTRAINT     X   ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         root    false    191    191            �	           2606    16520 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         root    false    197    197            �	           2606    16522 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public         root    false    199    199    199            �	           2606    16524 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         root    false    199    199            �	           2606    16526 (   django_migrations django_migrations_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         root    false    201    201            �	           2606    16528 "   django_session django_session_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         root    false    203    203            �	           2606    16530    fir_circles fir_circles_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY fir_circles
    ADD CONSTRAINT fir_circles_pkey PRIMARY KEY ("CIRCLE");
 F   ALTER TABLE ONLY public.fir_circles DROP CONSTRAINT fir_circles_pkey;
       public         root    false    204    204            �	           2606    16532    fir_details fir_details_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY fir_details
    ADD CONSTRAINT fir_details_pkey PRIMARY KEY ("ACC_ID");
 F   ALTER TABLE ONLY public.fir_details DROP CONSTRAINT fir_details_pkey;
       public         root    false    205    205            �	           2606    16651    fir_injured fir_injured_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY fir_injured
    ADD CONSTRAINT fir_injured_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.fir_injured DROP CONSTRAINT fir_injured_pkey;
       public         root    false    210    210            �	           2606    16661    fir_killed fir_killed_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY fir_killed
    ADD CONSTRAINT fir_killed_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.fir_killed DROP CONSTRAINT fir_killed_pkey;
       public         root    false    212    212            �	           2606    16534 (   fir_policestation fir_policestation_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY fir_policestation
    ADD CONSTRAINT fir_policestation_pkey PRIMARY KEY ("CIRCLE_PS");
 R   ALTER TABLE ONLY public.fir_policestation DROP CONSTRAINT fir_policestation_pkey;
       public         root    false    206    206            �	           2606    16536 #   fir_roads fir_roads_NEW_226dfa92_pk 
   CONSTRAINT     _   ALTER TABLE ONLY fir_roads
    ADD CONSTRAINT "fir_roads_NEW_226dfa92_pk" PRIMARY KEY ("NEW");
 O   ALTER TABLE ONLY public.fir_roads DROP CONSTRAINT "fir_roads_NEW_226dfa92_pk";
       public         root    false    207    207            �	           2606    16538 %   fir_roads fir_roads_NEW_226dfa92_uniq 
   CONSTRAINT     \   ALTER TABLE ONLY fir_roads
    ADD CONSTRAINT "fir_roads_NEW_226dfa92_uniq" UNIQUE ("NEW");
 Q   ALTER TABLE ONLY public.fir_roads DROP CONSTRAINT "fir_roads_NEW_226dfa92_uniq";
       public         root    false    207    207            �	           2606    16540    fir_sections fir_sections_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY fir_sections
    ADD CONSTRAINT fir_sections_pkey PRIMARY KEY ("SECTION");
 H   ALTER TABLE ONLY public.fir_sections DROP CONSTRAINT fir_sections_pkey;
       public         root    false    208    208            �	           2606    17613     fir_self_type fir_self_type_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY fir_self_type
    ADD CONSTRAINT fir_self_type_pkey PRIMARY KEY ("CODE");
 J   ALTER TABLE ONLY public.fir_self_type DROP CONSTRAINT fir_self_type_pkey;
       public         root    false    215    215            �	           2606    16953 -   fir_vehtype1 fir_vehtype1_VEHTYPE_3b51b3a3_pk 
   CONSTRAINT     m   ALTER TABLE ONLY fir_vehtype1
    ADD CONSTRAINT "fir_vehtype1_VEHTYPE_3b51b3a3_pk" PRIMARY KEY ("VEHTYPE");
 Y   ALTER TABLE ONLY public.fir_vehtype1 DROP CONSTRAINT "fir_vehtype1_VEHTYPE_3b51b3a3_pk";
       public         root    false    213    213            �	           2606    16951 /   fir_vehtype1 fir_vehtype1_VEHTYPE_3b51b3a3_uniq 
   CONSTRAINT     j   ALTER TABLE ONLY fir_vehtype1
    ADD CONSTRAINT "fir_vehtype1_VEHTYPE_3b51b3a3_uniq" UNIQUE ("VEHTYPE");
 [   ALTER TABLE ONLY public.fir_vehtype1 DROP CONSTRAINT "fir_vehtype1_VEHTYPE_3b51b3a3_uniq";
       public         root    false    213    213            �	           2606    17600    fir_vehtype2 fir_vehtype2_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY fir_vehtype2
    ADD CONSTRAINT fir_vehtype2_pkey PRIMARY KEY ("VEHTYPE");
 H   ALTER TABLE ONLY public.fir_vehtype2 DROP CONSTRAINT fir_vehtype2_pkey;
       public         root    false    214    214            ]	           1259    16541    auth_group_name_a6ea08ec_like    INDEX     a   CREATE INDEX auth_group_name_a6ea08ec_like ON auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public         root    false    185            b	           1259    16542 (   auth_group_permissions_group_id_b120cbf9    INDEX     h   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public         root    false    187            e	           1259    16543 -   auth_group_permissions_permission_id_84c5c92e    INDEX     r   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public         root    false    187            h	           1259    16544 (   auth_permission_content_type_id_2f476e4b    INDEX     h   CREATE INDEX auth_permission_content_type_id_2f476e4b ON auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public         root    false    189            r	           1259    16545 "   auth_user_groups_group_id_97559544    INDEX     \   CREATE INDEX auth_user_groups_group_id_97559544 ON auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public         root    false    192            u	           1259    16546 !   auth_user_groups_user_id_6a12ed8b    INDEX     Z   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public         root    false    192            x	           1259    16547 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     z   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public         root    false    195            {	           1259    16548 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     n   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public         root    false    195            o	           1259    16549     auth_user_username_6821ab7c_like    INDEX     g   CREATE INDEX auth_user_username_6821ab7c_like ON auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public         root    false    191            ~	           1259    16550 )   django_admin_log_content_type_id_c4bce8eb    INDEX     j   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public         root    false    197            �	           1259    16551 !   django_admin_log_user_id_c564eba6    INDEX     Z   CREATE INDEX django_admin_log_user_id_c564eba6 ON django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public         root    false    197            �	           1259    16552 #   django_session_expire_date_a5c62663    INDEX     ^   CREATE INDEX django_session_expire_date_a5c62663 ON django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public         root    false    203            �	           1259    16553 (   django_session_session_key_c0390e0f_like    INDEX     w   CREATE INDEX django_session_session_key_c0390e0f_like ON django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public         root    false    203            �	           1259    16554     fir_circles_CIRCLE_2d898636_like    INDEX     k   CREATE INDEX "fir_circles_CIRCLE_2d898636_like" ON fir_circles USING btree ("CIRCLE" varchar_pattern_ops);
 6   DROP INDEX public."fir_circles_CIRCLE_2d898636_like";
       public         root    false    204            �	           1259    16555     fir_details_ACC_ID_89c435b5_like    INDEX     k   CREATE INDEX "fir_details_ACC_ID_89c435b5_like" ON fir_details USING btree ("ACC_ID" varchar_pattern_ops);
 6   DROP INDEX public."fir_details_ACC_ID_89c435b5_like";
       public         root    false    205            �	           1259    16556    fir_details_CIRCLE_id_3040535b    INDEX     X   CREATE INDEX "fir_details_CIRCLE_id_3040535b" ON fir_details USING btree ("CIRCLE_id");
 4   DROP INDEX public."fir_details_CIRCLE_id_3040535b";
       public         root    false    205            �	           1259    16557 #   fir_details_CIRCLE_id_3040535b_like    INDEX     q   CREATE INDEX "fir_details_CIRCLE_id_3040535b_like" ON fir_details USING btree ("CIRCLE_id" varchar_pattern_ops);
 9   DROP INDEX public."fir_details_CIRCLE_id_3040535b_like";
       public         root    false    205            �	           1259    16558    fir_details_PS_id_ad7ef1c4    INDEX     P   CREATE INDEX "fir_details_PS_id_ad7ef1c4" ON fir_details USING btree ("PS_id");
 0   DROP INDEX public."fir_details_PS_id_ad7ef1c4";
       public         root    false    205            �	           1259    16559    fir_details_PS_id_ad7ef1c4_like    INDEX     i   CREATE INDEX "fir_details_PS_id_ad7ef1c4_like" ON fir_details USING btree ("PS_id" varchar_pattern_ops);
 5   DROP INDEX public."fir_details_PS_id_ad7ef1c4_like";
       public         root    false    205            �	           1259    16560    fir_details_ROAD_id_cfb73d85    INDEX     T   CREATE INDEX "fir_details_ROAD_id_cfb73d85" ON fir_details USING btree ("ROAD_id");
 2   DROP INDEX public."fir_details_ROAD_id_cfb73d85";
       public         root    false    205            �	           1259    16561    fir_details_SECTION_id_8e90b8a2    INDEX     Z   CREATE INDEX "fir_details_SECTION_id_8e90b8a2" ON fir_details USING btree ("SECTION_id");
 5   DROP INDEX public."fir_details_SECTION_id_8e90b8a2";
       public         root    false    205            �	           1259    17631 !   fir_details_SELF_TYPE_id_bc950e73    INDEX     ^   CREATE INDEX "fir_details_SELF_TYPE_id_bc950e73" ON fir_details USING btree ("SELF_TYPE_id");
 7   DROP INDEX public."fir_details_SELF_TYPE_id_bc950e73";
       public         root    false    205            �	           1259    17637 &   fir_details_SELF_TYPE_id_bc950e73_like    INDEX     w   CREATE INDEX "fir_details_SELF_TYPE_id_bc950e73_like" ON fir_details USING btree ("SELF_TYPE_id" varchar_pattern_ops);
 <   DROP INDEX public."fir_details_SELF_TYPE_id_bc950e73_like";
       public         root    false    205            �	           1259    16955     fir_details_VEHTYPE1_id_870a6bae    INDEX     \   CREATE INDEX "fir_details_VEHTYPE1_id_870a6bae" ON fir_details USING btree ("VEHTYPE1_id");
 6   DROP INDEX public."fir_details_VEHTYPE1_id_870a6bae";
       public         root    false    205            �	           1259    17603     fir_details_VEHTYPE2_id_fc3a601d    INDEX     \   CREATE INDEX "fir_details_VEHTYPE2_id_fc3a601d" ON fir_details USING btree ("VEHTYPE2_id");
 6   DROP INDEX public."fir_details_VEHTYPE2_id_fc3a601d";
       public         root    false    205            �	           1259    17602 %   fir_details_VEHTYPE2_id_fc3a601d_like    INDEX     u   CREATE INDEX "fir_details_VEHTYPE2_id_fc3a601d_like" ON fir_details USING btree ("VEHTYPE2_id" varchar_pattern_ops);
 ;   DROP INDEX public."fir_details_VEHTYPE2_id_fc3a601d_like";
       public         root    false    205            �	           1259    16699     fir_injured_ACCID_ID_id_0a33e27d    INDEX     \   CREATE INDEX "fir_injured_ACCID_ID_id_0a33e27d" ON fir_injured USING btree ("ACCID_ID_id");
 6   DROP INDEX public."fir_injured_ACCID_ID_id_0a33e27d";
       public         root    false    210            �	           1259    16700 %   fir_injured_ACCID_ID_id_0a33e27d_like    INDEX     u   CREATE INDEX "fir_injured_ACCID_ID_id_0a33e27d_like" ON fir_injured USING btree ("ACCID_ID_id" varchar_pattern_ops);
 ;   DROP INDEX public."fir_injured_ACCID_ID_id_0a33e27d_like";
       public         root    false    210            �	           1259    16692    fir_killed_ACCID_ID_id_42714456    INDEX     Z   CREATE INDEX "fir_killed_ACCID_ID_id_42714456" ON fir_killed USING btree ("ACCID_ID_id");
 5   DROP INDEX public."fir_killed_ACCID_ID_id_42714456";
       public         root    false    212            �	           1259    16693 $   fir_killed_ACCID_ID_id_42714456_like    INDEX     s   CREATE INDEX "fir_killed_ACCID_ID_id_42714456_like" ON fir_killed USING btree ("ACCID_ID_id" varchar_pattern_ops);
 :   DROP INDEX public."fir_killed_ACCID_ID_id_42714456_like";
       public         root    false    212            �	           1259    16562 )   fir_policestation_CIRCLE_PS_bc657bf0_like    INDEX     }   CREATE INDEX "fir_policestation_CIRCLE_PS_bc657bf0_like" ON fir_policestation USING btree ("CIRCLE_PS" varchar_pattern_ops);
 ?   DROP INDEX public."fir_policestation_CIRCLE_PS_bc657bf0_like";
       public         root    false    206            �	           1259    16563 $   fir_policestation_CIRCLE_id_85da1e16    INDEX     d   CREATE INDEX "fir_policestation_CIRCLE_id_85da1e16" ON fir_policestation USING btree ("CIRCLE_id");
 :   DROP INDEX public."fir_policestation_CIRCLE_id_85da1e16";
       public         root    false    206            �	           1259    16564 )   fir_policestation_CIRCLE_id_85da1e16_like    INDEX     }   CREATE INDEX "fir_policestation_CIRCLE_id_85da1e16_like" ON fir_policestation USING btree ("CIRCLE_id" varchar_pattern_ops);
 ?   DROP INDEX public."fir_policestation_CIRCLE_id_85da1e16_like";
       public         root    false    206            �	           1259    16565    fir_roads_CIRCLE_id_fd7f620e    INDEX     T   CREATE INDEX "fir_roads_CIRCLE_id_fd7f620e" ON fir_roads USING btree ("CIRCLE_id");
 2   DROP INDEX public."fir_roads_CIRCLE_id_fd7f620e";
       public         root    false    207            �	           1259    16566 !   fir_roads_CIRCLE_id_fd7f620e_like    INDEX     m   CREATE INDEX "fir_roads_CIRCLE_id_fd7f620e_like" ON fir_roads USING btree ("CIRCLE_id" varchar_pattern_ops);
 7   DROP INDEX public."fir_roads_CIRCLE_id_fd7f620e_like";
       public         root    false    207            �	           1259    16567    fir_roads_NEW_226dfa92_like    INDEX     a   CREATE INDEX "fir_roads_NEW_226dfa92_like" ON fir_roads USING btree ("NEW" varchar_pattern_ops);
 1   DROP INDEX public."fir_roads_NEW_226dfa92_like";
       public         root    false    207            �	           1259    17638     fir_self_type_CODE_281f125b_like    INDEX     k   CREATE INDEX "fir_self_type_CODE_281f125b_like" ON fir_self_type USING btree ("CODE" varchar_pattern_ops);
 6   DROP INDEX public."fir_self_type_CODE_281f125b_like";
       public         root    false    215            �	           1259    16954 "   fir_vehtype1_VEHTYPE_3b51b3a3_like    INDEX     o   CREATE INDEX "fir_vehtype1_VEHTYPE_3b51b3a3_like" ON fir_vehtype1 USING btree ("VEHTYPE" varchar_pattern_ops);
 8   DROP INDEX public."fir_vehtype1_VEHTYPE_3b51b3a3_like";
       public         root    false    213            �	           1259    17601 "   fir_vehtype2_VEHTYPE_d6246cc0_like    INDEX     o   CREATE INDEX "fir_vehtype2_VEHTYPE_d6246cc0_like" ON fir_vehtype2 USING btree ("VEHTYPE" varchar_pattern_ops);
 8   DROP INDEX public."fir_vehtype2_VEHTYPE_d6246cc0_like";
       public         root    false    214            �	           2606    16568 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public       root    false    2412    189    187            �	           2606    16573 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public       root    false    2401    187    185            �	           2606    16578 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public       root    false    199    189    2437            �	           2606    16583 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public       root    false    185    192    2401            �	           2606    16588 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public       root    false    191    192    2414            �	           2606    16593 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public       root    false    189    195    2412            �	           2606    16598 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public       root    false    191    195    2414            �	           2606    16603 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public       root    false    2437    199    197            �	           2606    16608 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public       root    false    197    191    2414            �	           2606    16613 @   fir_details fir_details_CIRCLE_id_3040535b_fk_fir_circles_CIRCLE    FK CONSTRAINT     �   ALTER TABLE ONLY fir_details
    ADD CONSTRAINT "fir_details_CIRCLE_id_3040535b_fk_fir_circles_CIRCLE" FOREIGN KEY ("CIRCLE_id") REFERENCES fir_circles("CIRCLE") DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.fir_details DROP CONSTRAINT "fir_details_CIRCLE_id_3040535b_fk_fir_circles_CIRCLE";
       public       root    false    204    2446    205            �	           2606    16618 E   fir_details fir_details_PS_id_ad7ef1c4_fk_fir_policestation_CIRCLE_PS    FK CONSTRAINT     �   ALTER TABLE ONLY fir_details
    ADD CONSTRAINT "fir_details_PS_id_ad7ef1c4_fk_fir_policestation_CIRCLE_PS" FOREIGN KEY ("PS_id") REFERENCES fir_policestation("CIRCLE_PS") DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.fir_details DROP CONSTRAINT "fir_details_PS_id_ad7ef1c4_fk_fir_policestation_CIRCLE_PS";
       public       root    false    2465    206    205            �	           2606    16623 C   fir_details fir_details_SECTION_id_8e90b8a2_fk_fir_sections_SECTION    FK CONSTRAINT     �   ALTER TABLE ONLY fir_details
    ADD CONSTRAINT "fir_details_SECTION_id_8e90b8a2_fk_fir_sections_SECTION" FOREIGN KEY ("SECTION_id") REFERENCES fir_sections("SECTION") DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.fir_details DROP CONSTRAINT "fir_details_SECTION_id_8e90b8a2_fk_fir_sections_SECTION";
       public       root    false    205    208    2474            �	           2606    17632 C   fir_details fir_details_SELF_TYPE_id_bc950e73_fk_fir_self_type_CODE    FK CONSTRAINT     �   ALTER TABLE ONLY fir_details
    ADD CONSTRAINT "fir_details_SELF_TYPE_id_bc950e73_fk_fir_self_type_CODE" FOREIGN KEY ("SELF_TYPE_id") REFERENCES fir_self_type("CODE") DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.fir_details DROP CONSTRAINT "fir_details_SELF_TYPE_id_bc950e73_fk_fir_self_type_CODE";
       public       root    false    2493    205    215            �	           2606    16956 /   fir_details fir_details_VEHTYPE1_id_870a6bae_fk    FK CONSTRAINT     �   ALTER TABLE ONLY fir_details
    ADD CONSTRAINT "fir_details_VEHTYPE1_id_870a6bae_fk" FOREIGN KEY ("VEHTYPE1_id") REFERENCES fir_vehtype1("VEHTYPE") DEFERRABLE INITIALLY DEFERRED;
 [   ALTER TABLE ONLY public.fir_details DROP CONSTRAINT "fir_details_VEHTYPE1_id_870a6bae_fk";
       public       root    false    213    205    2487            �	           2606    17604 /   fir_details fir_details_VEHTYPE2_id_fc3a601d_fk    FK CONSTRAINT     �   ALTER TABLE ONLY fir_details
    ADD CONSTRAINT "fir_details_VEHTYPE2_id_fc3a601d_fk" FOREIGN KEY ("VEHTYPE2_id") REFERENCES fir_vehtype2("VEHTYPE") DEFERRABLE INITIALLY DEFERRED;
 [   ALTER TABLE ONLY public.fir_details DROP CONSTRAINT "fir_details_VEHTYPE2_id_fc3a601d_fk";
       public       root    false    2490    214    205            �	           2606    16701 B   fir_injured fir_injured_ACCID_ID_id_0a33e27d_fk_fir_details_ACC_ID    FK CONSTRAINT     �   ALTER TABLE ONLY fir_injured
    ADD CONSTRAINT "fir_injured_ACCID_ID_id_0a33e27d_fk_fir_details_ACC_ID" FOREIGN KEY ("ACCID_ID_id") REFERENCES fir_details("ACC_ID") DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.fir_injured DROP CONSTRAINT "fir_injured_ACCID_ID_id_0a33e27d_fk_fir_details_ACC_ID";
       public       root    false    2460    205    210            �	           2606    16694 @   fir_killed fir_killed_ACCID_ID_id_42714456_fk_fir_details_ACC_ID    FK CONSTRAINT     �   ALTER TABLE ONLY fir_killed
    ADD CONSTRAINT "fir_killed_ACCID_ID_id_42714456_fk_fir_details_ACC_ID" FOREIGN KEY ("ACCID_ID_id") REFERENCES fir_details("ACC_ID") DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.fir_killed DROP CONSTRAINT "fir_killed_ACCID_ID_id_42714456_fk_fir_details_ACC_ID";
       public       root    false    205    212    2460            �	           2606    16628 L   fir_policestation fir_policestation_CIRCLE_id_85da1e16_fk_fir_circles_CIRCLE    FK CONSTRAINT     �   ALTER TABLE ONLY fir_policestation
    ADD CONSTRAINT "fir_policestation_CIRCLE_id_85da1e16_fk_fir_circles_CIRCLE" FOREIGN KEY ("CIRCLE_id") REFERENCES fir_circles("CIRCLE") DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.fir_policestation DROP CONSTRAINT "fir_policestation_CIRCLE_id_85da1e16_fk_fir_circles_CIRCLE";
       public       root    false    206    2446    204            �	           2606    16633 <   fir_roads fir_roads_CIRCLE_id_fd7f620e_fk_fir_circles_CIRCLE    FK CONSTRAINT     �   ALTER TABLE ONLY fir_roads
    ADD CONSTRAINT "fir_roads_CIRCLE_id_fd7f620e_fk_fir_circles_CIRCLE" FOREIGN KEY ("CIRCLE_id") REFERENCES fir_circles("CIRCLE") DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.fir_roads DROP CONSTRAINT "fir_roads_CIRCLE_id_fd7f620e_fk_fir_circles_CIRCLE";
       public       root    false    2446    207    204            F
      x������ � �      H
      x������ � �      J
   �  x�m�[��0E�]��D����6F!pzH�0iv���`�*sl��5?�����i��8�˧�f�߷:��2�}��#*�����W�����e~=�������a4�"5�@E!���g\�)�d|�pnҤ@�	�.��E�`����xk�G�V 'E�� �^��Ӻ}�������l��A�0:�H���%(�B+I�|�K^V`�r̠����2�J���a�Ƙ̵�T��j��ԭV̪mVwX1G�>��0&s�:��y�cu��cu�5�[�O�e��E��8��JMEP��M�W�n�4��W-'Vjpw}d�ѡ!���Ԙ�s����8�C���#Ɩ�QM�*m�L�7S�Q��eN��zg�0�~-�7����U	�@��#���8N�?�8�L��R�Wy��*���)�!8��ŏ��ZcK���"���IJ�D+���u�6�� �o��ލl��fR{7Rf���=���q��@ ���RI��W�� �y�p&      L
     x�m��N�@���)z�]���.]��<4Z[lcb�TN�I��%��^�L&��GP������|�u�� �>�(���x�E�Zdd��w�«�I��r�����R�.�2���fb����@��=�;@L
�F0���d�JT��ė��a[pS�e�7N8B۸B��B����|�땚�f�u?t���s�n���f�S<+n7^2bM}����L&305�Nķ7���y�&��5C��{�=������$�cpV?aEQ>`�      M
      x������ � �      P
      x������ � �      R
      x������ � �      T
   �   x�M�]
�0���aĭ�?w$���ƤdS���n�����C��/I.��Z&4Ώ��n%�v./Q���.ɨ\й�S���4����S����U�RBd���s�'SɾW�֠���y�Qk�s
j,������)1�jMo��[ԭ݀���z�����kW$      V
     x����n�0������P�Q?� �X��@����O�L%�3(ҋ��������4u�i���� `�O�Է��Wp�h_P���7��aO��2�zF�!+����؟�#�݂�B�p~ύ_i���.��ϩ}{{\#�RC6#�VX�H�;�����l����)����G7�q�ϧ+���t�N��SK9�ϗR������;���i�2[(U�}������c�K�XJ�}�C;Ns�}�rx���x)�P����K?�t���9�gE��K+���k��0�:u�pұ�����`�a����0�')KIy���{�K�h��������?��D,��n�N=]Hk@ʙN��ՙ6�#X��!h,�ʙ^a[�b��L�m8�R
��5��!,pT��0BX��@h�T�<��,�7{7��@8�h,x�Q�P�h����6�_�.3)W��0��aNC�h�����:�P�������P�W�W|����a��Aor�u;H��/\�d y��ʆ\�j��g$D��P��ny[�ٷ`P����8�-j<̏N�"��U:t������>��Y�C���W|6�fubp�����aï�~�r��뺲ڇq�K��ܿs����>�-k>6(��]�����>'��)��=�~W��G��g7�O���m��P�ϱ�|~�[�jm���Z��k�R�/P�W�H�g�k��hE񼲖��[h*m� �2�<H�/���:G�ո��C�x�Z����ܯ\|���eg���������q      X
   �  x������0�s�{/$َcCid�6�D�b[�'nbKV6�xc�雔z,�e`��6�`�}gu{��ͭ��V��?�o�u����N�eE�I-�qG�7E�i!�� Ib͊��I�"����vAS�۷�ɭ,�c�ĶZ��T���'İd���Ćar'j	���d`�6���Za	���]���(sP�<�|,Q�t��fӲ6ӕ�{��@A_�.��~��߹�]k�.���1��P��Uz�tg�ܗ�|�  �W0E��!�g� /t����ɇ^��O�3?�spi��	jw�7G���G�w�q1��/�P'OR�dw'In�:@���Id�����-�KW�,�(�-5Ow�=r�����p��$V?����n�`�(��!Bǟ!���ߏ�t:��yυ      Y
   �  x���Yr� @��)���- �X�AR95�?�4N<��H���Tx��X�X<��T��2!Yւe0�\C��(�b�����:�_P7� ��hӇ��< :U�`I*K�쫬��;�HhnB�"������
�8;�f;+�g�<u�`��|�<#Ӥ�<��VsG#٘j;��"��=Lx������FUz�BYP��AY�y��:|Zޜ���Z�T���S�֖��-�<����T�x��`u�ƃ�@��G%L���ցQmӀ�A���d:�QI<f���l ��^���u�FJ�b�#�C�	�L�G�?Sک�M��(`�����E������($r�i�7<!K�/����]�Af�����S��>��<l�_��3��L�h�F�#h"�dl�2�'tnO�Px�W菇VP$��2{�gy&�odAv�}��O8C��!4����WM X������2ó;7kI~���b�CEA�"�/]��Z�����2o�B�:���u��VprferF���'<�8c��q�_04�L�5��!�ņ����5���:�`�o���B�A9�n}���tդ�F� %=���G�͠��_����
50g��2IV�q� k7_Ӓz�\hs�Gk���U���(���A�'�M|7Ґی^���\�M^�>u@9�Ũ�H�7�r[X�ֈ�h�Sa����I�]aLMi*U�d��O��?�H�      Z
      x������ � �      _
      x������ � �      a
      x������ � �      [
      x���k������(2�*���`h�*:��]�&�W��MK�h6�+�/l�֮�?�i�]�vN�]d�Id�KKu����4�]T�]�.N�,��~n�6����*Re�8��l���U~U�%Q�}y��@�浹:Wnͩa�U�CC,��6�"���U٨!&�L��u�4�S��j>�w_�ڸTC�*{<��%�N��b���rUY�)�T[2}��R��!(冨�m�ӳ4Ҏi$�_�����K��o\L�����Z%Q�8��S�3���|��q'g�&�kkU��ݥ)U�z�Sl�E�r�V�|5M;7�9���N��\p�2/"rNtQ�g$����pU'��vWVmr��R#QG�;2���_��_�f}uy~��#߿?7�/�}��Q�ȱ� "G�����G�MM�C��J}�D�>NJ��Kq� ��Y�����{�͇6Z�����k�u��%uv�%��q�L����%;��b��hnzɽ�o8��zۧD̃��X�A��R۴������z��q��D��8���bJ	$�!��y���d�K���ȪQ2v��숵H��i,}��A��6��k+�u?��$����8.��l��tC� ��uYۯ=,^����\H��D���ꭧR����pª���
��!Y�QY'<u��Z�ki�R�T?���j��3��M�PU�$�[� $ۂ���Ш��Qz��ec��5���Nv[�,*�U)Tɢ$�-_qq�J��fB� ��g�yA��9%�����
�P�mm�/�ǽ�?���]}�{�2�\������r�(qh*%\��j"	�h%E��q^�2�h=;�U�E;�+g�6��E�eV �:�
�,�>�J,��ٶ�ϋ��qX��S�Վ����S�=�[�3VS��_�
���L= x�l{�*�X"�C`�.�Zpie�w�&h�Q*�$CG�E옑e���3&o��ib@�����I�yI��u�B�ZRƻ�s�E1�����f'��9�QV:	�UO'I�
Xz���DΉ��Ǥ��|`外A�����19!Ft�QCQ�?��5��2\U���t�-N_��a�.w�HE�����AD���ܪ�!�!UW4���?�����ჳ��j�'�ZÖ��>:��y��PnCU�7�{n���4���z�b@hUN|9��5���ԛ��<܇b��z\��l����M�m4(���BnhgܼN�?�ϋB��A�d����i��L0�ihr4�dH�S^B@&U%.j�Q��B2k��Z�x�L�J5El���U�RQ�w�g-��5��5b!��
�ĉ��"�g�@)V4��<ƈ��p5��E��Z�*-h�5����e��4�T�ل����"sE}���0�\�=�9�"G�/Yߠ�t�'�MB��|3!#��
�H���V��,g#���&��a�{WCe�K�Q;��M�j���nuQCL�M�j��b@F�[dU�n8���@@H�f�$�a"w�%�J�����U�Ȅ6����{o]�誒�����L+�v���P�YE��Iw�Aa]3m��U�S|r�7Pj���Qӣ�u
T2�:�e޺�aB�C�u���JgX8��W��Wܶ����#h*�#��@[�	�BDF�CM��zh/! �V���t*�L�܁����2�J����J���������LLݡ��{���&⼾��� �G6J?%(LP����#p�i�����zA)�qlڠ�{�ر�v�U&�5
C���kcq��
�w�( X?��f��C��*��Kս����܍��8=�ֽ�;��i>�Q��R!F�]޽x��c����ZP~��x�}��9�:h;wo����y�~�D��~�F�<%�y�B���{��<�8�N�RX9A�1�|��X4��m���Q�a�69S�o�*k>�☲iC���r�D+��pd:�,�A�8�G�����_��N��ƶ\Ђ�w����Vpn�P_�D3�Ŷ��}�ض(�#*�Ə����@^%[�\��JyX�M�}>� �E
��gg�+�~�*�5X�C��`�9�}`۫A����6Ϫ���z�[n]tC�)���R�0���B�U�k+%�ˤ�#+R����V��`�[}�A��^�'�x7��qk]��n7����!����ѡc�`ג�K��G(�CTȭ�}{LzlE�jD�~���i�b>n+�gj�4|�7�΅����H�n��S��j��(W����j������d[��4���i�Uw��B�SCL�m��CP��[f��.���3�i)�n[QCL�-�{�I��sbZmH�z�}7���Co��]����C%��-�)]�����.��'mt'w��PqC�{��g�"Rl�Rk񼁖ǵ�WY�^��<�CN��]M%n�;��&<�T2�f�]<�U3D�^9ށ�d�+����2�0���}��¿����>b]��#XȤm-����8���RB��x�.�6����M��`���ެ�V������uȃ'��Nȓ_r��ό � ��`�0'��`�DEI]��xګQ�G�"~o`��Q�RjM�g�Bfo\A�e�j4�J����e:����m�R������?�m�`u{߶�_VDÓ�抢�/��Y1앻H�
ao<$Ƭ&�U	�,�=4H��܁c	_�q���A5����	�`�y3Z�A���M\y3*�������ē���DAJI$�� O �VvHM:�컊�ưD��=�����2,��L����iAui9������X?J��ЪÖ�q�Bۼ^0�g��N��8��R�n!F�����t��L�oرf�8��̑���9w}[v�<eڿc�8��%��9tw6?�����}������դ~��ܤS�����&\�ڟ����u{9�O��^&e�����̿ط�/��(U�߆��څ�"�9�;�X��Ύ��x��.���C����Ϡ]n��_����>G��a���Ө��C�A�C����C���0D���|���д���iFD� ����>G��zr�c��Uτ���yI<d��{�;Dl:h x�X�F��1c�������w�2S�]^�:��� P�b�u�>���֦_���qG���	(!&���o��DG�?ۊ�H��}��<UH��r�@n;6s�t�y'J�F�����hm�v�sq��g��6L]���5ʐĞ�[J�LZD���DZ5�(��c��� 
�I"���ߎVh{�'���g�oG7���эX��W�	#��i�I��rg��������/w���5��=���f�bq��{?�׫�/f�PE�o�<@��i{5��.B���,�ſ8�ٌ���s1��*�՝�@�>o�gfpȁ��MCE��R�A��N�|�'a�-�o_��ڮ��YU����W�Da�g{_$�m^�����q-?)�^<�6�R�k��r)�l�c~�uְEF�K4�˸�^��w/���=��)d��:����I��7�|8gk:��B���}�����[�1o�s�HQR\1��k`r��k�~�ҵค"���J��9�5(K�{("rJ\g( ���!͝���2C<�>�}��8��dVӟSWyDFN��^~��髭�j�$�9r'��쌺���1#�}�d��Γ������4���/�lw�^~��Uh(
���IZJ����I��{V�D�k�ٸB�H�M��
�N	�X�ेHZ�����N���z3�p��7!godZ�D�.�K/Ǝ|��J�U)фRB��j��:��|����쇯}�ں�jB�%Զ�V�-�7/��Pd	���:' �b���?��/�Z1�(��PHI�j��c��)��P2}3Yj���C��_����[�s~6�p�-0����^�e��{��td����`���ߌz�*?ꡫD��q�������$�ܔv^�6��;a�$6���$�NJ�_�N1����
h1"��#<���y��߿���Eh��0�o���2�tVxL�w�QCD�͆H�ª�Z�w%V��f�IaUL�F5��N���F}ס������D�F��u� �   �p9ߥ�>˟����Un�Bn��ɛ��.�gݷ٩��I~?_u!_=iorCrÓ�*[t![<���G�G�3�n�C���{�/�8r3l�R4�8�ܮ�����I:w�o�!�����d9�lf}RB�4��I�d9��;Z�&f�i$�|��0������`�1��� ���%���))�z)��Z��7XÃ���������fb      \
      x��}ٖ�8����+�t��Z�.[��G�RX�����u��;.6@P���8��*X�8�  �P�{�g��E��~ߚt���<��;x��G#4��d
/@Q�Y�wS�?��ځ�~_�g�����P4�|�/m�f=c���7��f�6����k
��wK ��Me����8��t%�t��ջ~gn�ݐ5�p��+��qUȐ�����s����}��W4�����v����d���go�k���+t��}�/�ߟ�+�%k\g�O���gox�(��T~�]12�p�8���e>�X�׶���I�8Wp�LU۩�@���̆��3P���6vf�]I��3����F�3��pf�ے�$7��/��F���wEQ4�{�i��'2E�5�1r���ƌ��:bv.&�
�2�0�&}������g�c���
��{@�Ɍ�f];�����6|3&���PQ��y�Y2b3�Q8#�����d\���WSt#ƅ��r�(���
����-�Q'��>��A���H1-���i<�ƺQ�en���m�v�\���U�sdum]�@D�H��
�϶W`����`�DW�+��UH�&�Q���KB�5���J�n�¥���I��4�8�CCҤy!�=���v��g��knm�8�$10ɮ\�r�x������i��9-ZM�С(�6�Cx���+���]���W���h�6/SIv�Mә1�+�X�y�+*Zʂ:���Ͽ��V�?��@��5�B�R榾h3�1��!�I�i�
���Q��/����`����@�dMi�̝f�~�*�����(�$Ze�1t3�,�lcI��Ч���1�D2�Q,� ;x�1@$�B_$��f�g�8�H���)�)�i�UÐ�@^[bئ������%D��)M�ԏ�9 �:o��}�Ҝ�$��.�������4�qp��1��wڣR�ƙ~:�%�M5�>��&�4����)�(��j�GK�}��ZBBOHqȭ��� �ZA�Q�`��E2�>�(u��81 v��QA1w�/�|�E|����SϿ��ط� ��U�5E���aw���&�4����N�~�	���M��\
ZC[�(:,^�b�1X�V���1t����>?n��y��a��L�d7��a���m	:��b����F4a�-�����Es�̝hub��3yl�@>��_rH��aqlrmE"K{s��
XZ�As��ӂ�z(S	�+�t*�ćc�8��w�[ϓ��9�K�x���+��7�$�o��U��c��Ɋ�k�0خ�'��4�<�Bs���~�`���g���+`D�%MY�\#4�+i+{�ߒ��������&�+�Ħ�q��T�!��m��W�&�ת�,�]6�w��2�.G��7��Rs��,&�o0��5��%��`+��
zug�
�=�ibM kl�y�Pg�u�W�]���G����9�$��ϲQ��CWp���ޔ�v�bL�c��R��k5]o��&/.
N .!gdp�l�  %Au��3w�ZA�CR�7����!�֠{��ms��ŐRbɖ�C�1<�T�5 =o'{(jRs/�k��t� ݜ��'$�.4�xRD�S�Rh?}����WjJ��a���|9hF�^������۠�i1q����f�{n���#��ͮ�«�-+^����~�/���0W`�A,�C-��d��jJ�-���v��?+\�m�-��X�~�";��,�Y�Ơ-琉����˹{�X��5�L%�q�ᥩɶ6��Iӷz��t�u;S�-C��E;�� d�f�����f7�];��$v��N[�e�]�;	��?�~�oؔ�v5�B;��A5% �.��L�޻z"��Г�Ob��q�Yh�Q�⁔���׾�=E����n);� ���i�3b�!��9�[EY����N8�B�Z:�@��d�c�iː}q%q�Ț)�Ng[�J��ZJe�i�i��&�|/0�YU�2P��z�gޙ�b�0�<�N�Q}g;�~]�F�1��3p۝�bνM�����~bs��X���Ba�	�Q�!�p*��bb@�<��'(IRÐx���kٴ�
"#�M��.�e���L0�
4�_�6�Ye눹�n�ZRWi`�n��vaN��x�v��cI�(�/��V06��F���e<j��Ne�u^A�^4"��֙������D�nt�3w�U�v�Lw�$8���~���
� ������ ,Z�h�0�{�ͫ�8��&��L�dSO�c��KP��L$+������7��������K졡-ۚ�LG��rM���7�������w>��$��a:�ʅ�O!�<4 4��/�J�\�P��d;�N�u�w���x���q��3�e��jk���\�h>*sSS�r�+�j/�Z��ni��A ���ᐞ̈́�Ǟ�]�����B׆�(�JT#&�\A�1U�����2���挻��2���ѽ���F�J��CƁ 	gʻzؚSm �:�4�in���I�3'DɢG׊��a&;�dZ��{óۿ�퐺�WX�آ���r��(�Jv�U�$��KeR�g�?DkD��<�zJb�
��D��kꍎK���	�x�Y0�q� ,�q���{8m�h�o)/YC����mSҾ�������fe����nn�Ue~�tw��`�F�k�J�`�"L{d�D� 7�q��[�K5��#��m]-��d��{G�Dv1CfmB�@g�L��r��,����F���;�Y�5�>��|ڗ 	ݴҿ?a|���j�!����)C��y�Y
�Q�,��+�e����8����mծ�'Se������E���p�����Kߦ��
��/�uj)��軂XYIr�SeQbi��41��#���Z���\�qb�����~��`�D�F#;v��	�sΰ턒�͗*�	�H��}G"�u�a时!/�aܥ9�b9f�c��n�Mz%�3�>��'��q�3��v�V���3�m�iau�
V���[OU��v �W]=��nF^��]�q��.$���b�ZIQ�j�w������pV�g�%/����dǨvv>h���C�7,��a�y�ٕ0�ऴ�5w�r7�Mc���A��h%)eY�3�
�y�m���.0�#���k~1	��:�V]�$bc�v>1���n��4�~��DUߩ}�+`�#����,�z�E��H{!S�d�81+#s��<�f)��@��[m�"��s3�iN�vNi��ǉD}�[ɞN>����X��hF�BC�>Y�W��r�����d�ҫo��7E<�yX9xE}�	��
$ֈ&��i�}�a�]�`╛h�UF�����ڮ5A%{���dك@����H ��k3܋Ta�A�`ߝ�j,=9F��%2�L��3y��w���Q\\�\�:�G�/��`�v�Hn�F�j���|��f�ib@��T$ ��������fG;ln�9�h~nmE@�d�����@2Whk���K|�'�и�hǟ��h;���.�������7ǶJW �l��)&;�@�(�;_V�%9a��/�M���ȹJ�G�V��v]����@f��1c>^��4;�jϑm�+�I�u��)|$Eeh��7y���j��_c�ݾ�鸝_����	���§���pM�η��v!�{��Ot5�����E7y�F[r����=2��}[�-`י+�^]h�S����_ھ��_�U4,��V��UDsJ� �������ym ���gTИ̓��sR��tY��z8ͭ.K��ӫ��=���
r<X�X�P�4�(�|���12�[Lj.*�����&����zښ�zj�9u��k�������p;~6�&}>�Nh(P�[�d\���e���<���Ҧ�C���x��+3�xZ���h7.T�9���t�-���2��]q$uS�`�i���e���~�}� ���M�&�.e,:��>vQQ���U��G͉%ӂmq�5
*@�+�˃k� ֖g=)T�Ngo���F�&�3���:�mE"\L�a���L��x^O-�jِ.�N�w��׵#���� ��|�@Eɶ{r�2[�k� ah&Dx�0`>�J���8~$�6�w,:��LQ�>b�X�0(r    ����k!J�� -b�l�U<ؓ��u'�i�}̀�Z�ݨ��I_x��=�dښ��H'�ر2|�W��+p��Ũ� ��x�o�C���|��
�l�K~�ك�m���굗+;��ۮ�������š��T�0�+-; 6���at� ��� od�������i��H�����ź��OFl��3W`�Y�R�:��4�u�q2s�$2�=�������A�3�(�%�p���(`�H\KnYFcrm���Rv��s�ضl�Ju����
.��`�~��p���$�ae�P��վA'I�7��\���|o"�(F���P�� FJ(YD�a � ��v z�募s���3�K�b�ϣ���ҌP��H��`�^�!"Pi�%� k�!8Y3֪��W�jٕO��O�+���2�D	h���ح���D��\yp�z%p�$Z�����h�o� ���A�~%�r+���O:cq`�!7�pfK�*��h.�QȀ�`=�Hŭq��-	[�{�2F��.p�NPz����A��c���,� �i+�fpP�b�x�ɚ�����M%p�%�� �rvC�1Z�i�w8��w�C ��m�m�P��W����'���wW ��W�jĉ���{����mK�cI��3=Z��m�g~r�s�+دm:}$x�����@D�13�!�XJƀ��E�o�01*��W���B���M"Q�������L=d���#Xg���Mv�h�қ����M�W��}�S(R߈Y5LĹ	אS�R��	���A��+ l7ϐESE1Ёm� ���!bf���!C��(w`�:?u����l��
��I�0�#^;�7�pd�b�J��,�bt}�#��x��h�;T9��B��:�GQ���+M@��_��=
c�|f�����n.$V}�Ȟ�uG�gy�(��`�h&æW��f�Q��mb%y��#WC}^���+�vTg�;m���ѢYe`o�U����
�M-�m�&ΖN���E,4'�ͮ 4��n0h�Ns��Ke���:Ӯ K�h�Ų�g���E������`~ag�T��^
-��M�|���x(�y�L��B���ﮰ�4aiB�����b*��k�����1 ��2�+���iu$Q�O6� �A�棱/<c�P�˥0r��������E��l�؃��ȿ�>(O���2簯�oٗ�B���/ �H
�M�����f��l�0}���~jե-��{q���򉝺��$!Y~���g>�����'�ȣ��/Uj��|5���������H07�4��7�8�yA�n��@
���r��k>���!���Udn�+]�������#�=/���K��� ��'X��.e�d���WWPS�����������c��s�qT�s�k����ܷ_|Mp��pj�iD�9 �d��r�'e {jf�0��rj��-�a�ڧ�O�FMsU}���ւ�wq�)�!NJ�φQ�U�R����(ħ�hh��!(�{�Qm��1N���?H8�	���d��f;(4���|/r_�#�k����n�DH�m�v9���{6��"��OH"���?�^��h�i(��
��8�c*A��:.2�?�8泄*v�<Vw�0��W�=���=@�x�,��?f��6zH�WE�vâ��ْQ��v����IW�̇%���Z��'"��1+�+(N�;Zp��1w7˟Cq�2�.�6q�A��fk��
�u,��9<y�Q��5�B�B	�����y �F|��[Y�l���5Cj����ja�3)�L-|?���F홏:����8�C���E���ę��F+R^ck㓟5��KE��t��Ӿ�(��«#�R�p�H�h��!�Ƚ�4���Fp�}��1[=q�w_�!��%�`����A�4�)��װ'+C���؃�)��Bv�\:�}2�8in.����Q`[�
,�_�'2F�,8[Fq�I�rdc�����H��e5`�W?"�%i��
�=6�x���d�ۗ��5֖ǋ.��F������]�U�GF�/	�Jy^�����^�.��Џm��.��(�>{�>��F�h��mnt;Z�w�4�m0EWC�3�ݥ3��*�n|������5j�P��Q��!jtk���cd�EF�vD�L�|m�1�V_t�)V�pPR�v4��v�*	�M{�^�ҳ<v��HϺJ�}xj\.���~�yW�^ԚQ���>�{�
�l��B����44y���X��ѳ���Y��[��f��i�ā��7s��w��#.+�)-��V ��W<�ĵ�j�k�^)^��sG����J���5�6W�"e�Q3�9<0�:x���;��C �dC��[}C�H�����ڸ�U���`��Kp�5�D��7�:5��G|8N?�=_�Pg� ���v�i��H}��+0Քr �i�<�J���,Ƕ�`}�T� L�rX,n"����ky|������U[ʱ����WxiO}\=9��OU����ª�M���0캂��Eg��Y0>y�����NX�MlP&��#��u�p
�{�|k~��t#<^d��	�c��_|ږ��m�P�|��%qJ�5�X�pF02Y!���F���0�mBD��Bo�*��B���t�[��j�tg*g�D�vDE"�҆-3<Z��@ls��#zR�$�u�J����+�`i�wR�~pb�G�+����g�ڛJ�*���[�������9�)*�^|X��� ���׋��\5�Y3�īH�c�)�8v%L��'v|]���[AK�q[��7챱GhL�]GJ�G_dM:�fO�3�#�
ǔ5{ �i�s��A�{�w��0�$b6d�h�<��w)/�
z^�m��⌹6�%JQ���{����%�F&`��9������%I�{f���#�^}�
9*��Ƣps,��AC`\�ES �?.*�M���4(�-f4�᪶��)�aG�^G�dI0ۼ�QY����J�z����e�*q�p\#�6���鵛z�k�˚B���+H�L���� y�\HL+m�piX+��kٱ��@��50�n��mS\a���Rs����O����׌AgW_>$�FcU϶Ů � �:���δ}�
�'�����q�8F�8T�p&&p�c��e0���Ȕ'G��������Ξ+��<��������+,e��wԟ��X�?*��/��0L��ſT������L��^��gop5��a�(��\ᜋ�Y�	�s0��0p�H�f���X���Q)��q~�J���NF/����NO+H,����n?��8ї����iIMgP�@�h����_���7n-�Dc/��'�*��zX=���%���\0e@�@�)�6@UF8dݘ�P��$�{��m���5*-�+�A���Ֆ��G���.nM;����s-�j��~xs�}Y#�WXvĝz��G?nyA�	��
�':�6r���)���#|���1��?#ǫ���(��2U)G��v7JA��W��c�m�����A\8jӆ�Z	Js^z�K�9�H=�4���p�6�����LjПQ��g$_R��ڜ1��� 9�f�^���4v3'|rX�7<j8������"��Q��Jv0��"P��o��������o�ު�Y�J�	I�l�b������#����Y����H���������hx8H�z�l�\��*a������z䌞Fg;,��$��w����p���O��WK�<��$O��6NSc[b�e��.�sHk���d?�`�AOQ��v�-,�>Ŕ��_ؿ����`��8�=5w�4�����p���py��q1@��-@>3fT�F}���p�;9���Y�q+��lޢ�^E������'Ɍ���lj��1�65�i	���E��̱�V���L�<4��c�%�L7]���W�+�>��'���b�f�%��v1�c��7�٠������F�$Q�Y�Ľ�ލ�uײ͋�P�{N���    ����g�`��A!G�Xr��T
ңE��w� 6}��+��LsS���b7��nB�_���s��Ll$���2��9�!P���<��t�ϙ�:�A/��~�i��l�4��I	�gW��ۤ��t��> ȴ��e>@P��&�I�G]�ǋ$x������8��eF>z�,��9#���/3�&��m��y��b@B��,��j�����ҶΆ��R��KC�Ј��+'�o-�Wl?3�Н�A�K�@	"���ccQ�"����u�K,b�Yw,�*��LsD�������/V�k��}3��g'���P����/ovu�w �3��A:�l���	;���Y=w��WX������pu���O%�GG�����C�ς���>��bmI<��y�L�+�V3��+���f3)�+�6��08/�%�E��E�~�<��{�>a��+���I�8|o�"RE�
�h$��o����^'���
���h��oQ���a�tj��q��.NI��8�~;{�y��w��>We���~!�������?�֒�j���:|�z���_�MQA�`�a`�n�6 �Pd	4�2����J�^��ޥ5Zp�)����w y.��&-��.��
�LZb]Iܗ�E�V>���5��uW��-bf�Q���������fz��ҩ6$�¯i}�g�#�f��P����^2����>ot�9��:W`�/�\����DgG���Z:h��6��%��iR×�o#6ܘ2v����E�#�
��n�o���U�
�,�fu��hn}�,̘u/EJ-�>uF���+@���ڃV�
�`O�h��P�6w�O'��GWx��c���p��d���0l~�-~����%���6ʹl�8��<#����'q�yA
 �B��سV@�+8]$ ������M�J��]��X���j��B����&��(�>9�U�,�v��cW��s��
���X��[bI� �-2{/6Z>I�~x�kĖNߨ����2i�J{�3|ہ�c��0Zl{�e��o}b�u1`���-�MNg����^'��n�.~j�b��_�`��'e�1,Q��p_^8 ��e���`[����_I���lk�lkt��� ��E�jJ��'�E��KQd��/���T�4(/�/��b�J[���1���$<�	40��^;����O�i��һ�g` �Fin���z�0�}����m�s.i48E�Aö-��1x� ���X���"��]E�²�h�|u��<�in��fM��'�{�J�Ճ�}܎Q�A�w83���z���[�{�	]!�b�����6鶝ϝL���v|�|��w|<�� ��4x�	�kg׌��/���U��4Y�_ :P�2���@��$�'�um�i� [.10�f�%�d;+�̪��IJ��p �3���f!��m�����я[���v�z�V��m>Al�D�"'w��x���*Jr����'�+��_H��@�����)�� O���fƞ��05y�29�y����ċo�0&xB��������"Y�Nh+-�0>:Y<TM[U,����o���������!���@��+�����2��}�
|����Jo���k�hL��V%B�\�R`i�����=vU��&W��2�{q��CX��&���J}�M1��������»�`��J���� �W���~����3�wR~�y^A�"jv�u=I2$@�k�2�ZBplҐZ�+�|�uR<�1_��������b۩�ɩ��<�3E�p��~pCu^v����"G�4�e�� ��[U6�9��nv� ⹑l��%~qA�:��W`:$����Ĵ���@�G�޻B-�>y(�ް��ɭP�3��1kID�=����a��m�{�y�r����� ��ưp��盈^>ߴ �:� (\��Y,���-��	�.�T�9R�����c����OF�֠o��fT��!%��t��Wa|B1���[KL�̔￐J-,(_~!�i���O_H�~,�λ���=��K��o?�}v]4O�z ��E	��L�>~��\��/ ��8�o��J-H�*Ker���
��%V%�i/�MKmt�Ȃ,R2���P���~ij ��/�`���>x_�BՈPݱ�-��^� i�k�y�}�Ί�8�����,�থ�V6��<�L��	{ش�v��0�|��1���8{Zc���pW�)px$7d�6�}d�����9>b��ͮ��ȷ��2Z6��2��7{\ǰ�IDZ�'��i�$Ӄ�������<,E�C��������ed;�
��~�Mó��<�?
,q0�T�?�x*��"����=^Ҋ�I)N��%�=#6���[�j��#C���]oAk��?�츱�<v�okajr�
W�C/ƮA\�}�2ű�'�{�!�Ô�$��]�e����\����g�ڱM�f�6��C5H�fG��~,@����W/9	��d���s���Bl������⋑\�;4b)8ÞO����G����z{xD�;\��S,�e3�őЀ�)-s� ������M|���;�a���/lDtr���Ǌi,oT�E>l�8Ne�����c
v�͔oNh.�X4#��;�p��t)����tGĀ�W�h>��]�� Fb�p�l�咏�0�tW��>�Рi���i�M#4�g�6i�shu�\ݭf54:*�q�(Ͱ���ގ�+��Х����nl+�Es��gФ?�M�����sF�ѮW`���>�N�s�7H,e=#�sG��ӥ]Ht�]A��S�+��	�c��UG؏D�}�Q�kQR�-8�nm�p4��@&928 �rwl	��m%"N֘�����{p��F��x�[ֵ��p��7���ѼK�K$����H����{�u�<o�������$�)�ɕL�@��z_䗥��0�ǟ�v Y�w��������%n	��bܢ<�14���A���b�`�C-��/��-Ŀ ֜����9zߎ���G��^�2d�^\#ޕ��
7���P/�ņ�#P�by���i������'��H��=<�S�5� O�ߪ�G2�Tnb�p��d@J�?GL���|B��]L|r��>��rEdG��,ACKN^@�#�+P������������&�6��Je��b�u�Z��i�S=�co����fY\���:���;T3=�9�p.Ϫ��x�ΫǦR���XAs��q���_��)ir��A��D<n�ϫ�}�l�3"� ^��d���� ������q�[6�Uێm�8�˖�wk��C�XlXq����H�Q|�-ؼ�H�M��V���޺�x��|L��o|���q�m�^&Iy��������|���� Q��LaZFC����u>���1P�u=��d���qu�:=�(�MZ���������oz�T���+8�Մ�m����C2V�������ı���u���D�_
�.�A��W�G�G��{՞׸3ZTP�MN����+/�#��?�XW�V�auȍ
��3?i�w=�Sv�g�Qs�ބ-C�'�}b���6�%�`��q\�cCC|��ڻG��� ��e8���
:���9uO�wG�x�0����ϋ�j�؞�»�қ%/����:��ھ��վ-ۻ���ޘp�-S�g
�"�y;����+���ډ����o�c�
?�~��ҭֳU�Laѓ�^nN8�/*�������]߫l������7n%���4���v ��~Sf���#-� O��[�X�iz_R�!O!`��R�n,c4� ;+heN���L79�/;I��p{���Z�bH|Fm���f���U�!�Ȍ�@�����|ߚ�,�	ێ�:i�P{�x�۠#S�<�$/�y���a��[8ngv�qR?4���3��j�]���!��XEu�|�x�q��1�& |�'�o��dL�0�˱	�k�ʯIĒ_SP�ȭ	D4#��W?ğsj2`�?���1ܼ�Ϲ4[�̷�h���͡	Ԃ���3�枧����t���3�+�x�? h  $f����ܙ:"Ϲ3�b���ܙ��?��q��ʟ�f]2��7y3AtX��7y3A�̹͙9<��-�7�F5��%�X��=�F���p�������i� ��6Luć����s<26�`��d��
4�%@����"�~���'ՍO}'�_��{?Z�c(�ʪJ���M��	B�`��ǌ�6�ţ�]0с��~��c�ጡ��x����y�+�TQ�!`�n��bd��٧癩lyhZ�Xp�-�}0�u�;�~;�ﳔ��~���~���O���O-WSkok}���j���bz�Ab�^�Z�{Ll�����п�����><o�O+u�~���`����2*U��q�ň-�
8��]�����'����va.�� �� �.�WA��,w�?����R	2]b����\,���]֦t_���Cc?�N=$��Ƹ,���cb�t�D�J�)�u�	t˭�1ߍN��LT���=x������n��]z=���6�W�#H�p�i���+,�j3a�0�0���A��	��\��[��ʠȵg̲!g���k'1�
���y�[�fUrR9���u6���7�j#G���g�VP,~Y�~��-�#����3��5���<ed��ʍH��v��})�j�� U�5�+ǭ8��-)T팟����^�`�<��hOÐNd��D����'Q�tT�[�b�7���7��'�I�+�����W�� a8͊-�C���j�P�OÂ�u,��p<�,X�\�ʑ�-�\[Z)Mq�th�@~�8�m�~D�7#�e^���;�
��a��=�\��w���O/�_!���%�����B�4�#[I�[^ -�@�-G�Ȥ���z�
pk�p@t�qf��i���a�c϶?��6\���P�\��A4_N��ѭ������/��w-�N/���'� f�oO��ۻ�ᨔs�db�m9͌���.�R��irh�~\����?�.�����ث�8C��%��%���)��*����NWs;������i���d���*@g7��Ô��t�Ɏ�+(�7��n$3Dn��|	���>{לU^�?Z���v�uVgZ�Y�uy�d~��57�C>m���N�dz�X��̐c�D34YBT�u<������Q�3w��4�.�QŚ�g��u2x�X|a(EJ�
���iz9�q\!uo0�TFL�,�Ɇ|v�Ɂ@�g%�&��7�]'\�	��j������������(�[\�I�ء%�9�5/�<9�c��.��������简��=f�輠X��$����|������8�r��!�@��R&鷠����W���uX�c`�]��w%`y_V��32*�8Ĩ�4�X��vt/��_�$\7 �'tR9M0شy�)��f�������a���2D��f���uN�ЁYM�	�6-}ޡi���������¡��TY�?���p�7�88 <��SroKwt�J����2.��ƫ�]�	��'�R��_л����:E.���P��<�K�%��Z�] +� �4��e��\=�lwm;:��qe�5/jum]$2;� V���}"��W���hoI\Z>�>�c��ZD���
Lǜ;;��T�-�%8+�-���?~�����      ]
   o   x�3�42�T�p����������
��2	�����9�=}|\����`awN� �0O��`.�����#Xʍ��1�ч�f93�aX���0-� K��c�;F��� �$,�      d
   g  x�ePKn$!]�S��+�I���t�\r�j����c�S���H��g�o���^W2���)PU�P�rH���)Irٞ�Æ\Q�������ss(�O{�xa�m=�M�yM\���'��s�]��.�ߨy��]η��*DvM9;����3������$�ɼA�!R�����;��򍦪l�gB\��=�;�
wC�I�2.�u����5?�k'3�	�g%.�6�+�$8̛i����f�g(
��7�{?ѵ�V��-4ٴ��7���0h�I�`�W�r�����>w!��G�>s�n���B�73�jV���Ř�+�C��S��L���(C�]����'��d���1 ���      b
   B  x��Y͒�8>+O�io����x�ǡ�U��ϱ���t�0lm���,˖,��<�ϣ��<d��&GV��%��(��Hm��(+. ��2Y�J��DZ)9eV(9��N1 v����u 9;��dӟ��T �].��)���>+h�0@N�u 9�(��,1@���Jjԙ\1���؉1�	z ܺ��=��>A吡�סy�%5J1@��(��a���`� �J�Pr�� r�h���� �=,��qҩ�Ō����ϴ�,yX:/���p����r�ҥ�8���ݲͿC��Jw��a�X��I.�2�Z���!�i2����SH��������][ܰ��M!n)�1n)����Dc���nX���`|�cb�H����C�D��szInlB~8Z�cb֥�PF�*{�1�1�s;܈a�����YZ+>�-��=��a�pd�7�xN?b�G,�Au�[��SBDA#�i������4F�ȑ��k����my�X�c9F�1�J���x��e�o���jwjq(K�����½��v2D�zuʪ%�Er��;�0����fӇ	�t��^념ƂWWn�_��Ú+�nǳ%||�Pk?�F���GZ�/ڲ
%���
����b�e��h��:$X�f���³=8�B�j��-¶���������V)n�>{�[�=����I���F�{��R"��Ē�Kw�=���x���׼�_Φ���ӳ20��0�2��YV��3��P}���gR������n����n�y��G7�F�'T��0g	����j����}�±\��/�@��ث֋0���\HŨ��oԣ�i�C��Q�j_�Y�b��5ݮ9X
�7��S��'�m7�D�;��A���i������R�p���6�v��+R�/iVV��˕^����b����D��<*�<�ؔͮ<,��������U̻��4��ӗ�w,�t,���T�{��� ,}}z��˅jQ"��]�*�+�W����	72��X���I�&N��й#ڕ�����T%.�w�jD�p.e��J����E��p=k�y��`�e��GN{+��N�0�D?M3�pJ�<���>���W�;b�m�m5s4�i��lq$+�c��`L���3,�	���W}?c�m ӴL��M�=Im���h��{��٧�J��ÿ!�?b<w�V��0�]�����w�z��4��w���:[��#)��+Q(���3�{<[W�}]<��w/;��~��6p�^8I77U�ͻ�n����wnʋi�\�pa����D��3����n�g�?f^B���9��3#�9�Gr�L�#ѯ��y��n;t      c
   �  x��Yݖ�(��<�W{i���˘0ʆ$�:}μ�s�W@4��qv��9{hPTE��G�3�{AG���Q�F5�v�u}'���[iJE{�����ܫ�`�,;�J-4T�J2hh�6�Z�A2h����v�o ��d�� , h�N��I% �:J����}�o �-04�$1��v/ Ki$|�ɠ��ܪށ�G�<��o��;��j�0�� -e'%�ӝd |5� hX0��� ��7ɠ!�0���> �(!�& ��A�]%\��(��B����r����uf��N�*��U��R�c�[l�A,���V祸����C	m7� ��(��✢��}�/=��e����a��̽$�$�;M�f  ��X�T_5�%3�f�jGr��x��#��J+����-M�\��4�����b��E1O&ן'Ӧ#\�xYt�&����n�a�x[ �8 H6P���~,`����%�i��Z�C�,匹���dV|5/���q��V�Oo����1��3�VW �j3P��z�R���t�˿ �ִ�uu�Y͎h�z�\�ﭸ�=��`O��`�NYs�:��ך��˳��k��-�f��'���<��%Э��BB�bؾ����*<;�Bɣ��#b
���v���B��؞)�����<����%�+Bk|%=@h�`�ͷ6~mM�}݆������@l8�0$�Fp̱D����l��p��s,�h�^���C�O(��@�ƻY�]�W��Nf���e+�� N%�����Y�"[�]��>��f���u8yA�<oʐ�pz���zp-�	{4��Ua�or�(�Y:W�k\��
SZ�~���7��h�U'��`�|��,gٰ7�M]Q���0@&��\Y��\Om��H��H�2����H�4n\���bF�dO��X<
��%Ɵ:�I�c�CL$�6�6%;^�[�<����;ǿ�ӏm�E.W8�~�\Ҏ�`J#\1x���n%�Z��L�i���6��!@2�	� �-R$nu[�H��JB�v��z����{QO�s�D��$,VѮC\�Q�IL�ş����Hp�����qt�h�(k�Ǿ��{y���P��^��:/����T�h#X��5��Av��g�4MȇE�нR���F��ݼs5���㦄F�K�����~%#��o�fMw`���.���[�w���U/�>+.3힌h���H~#닋�>���E��t��_�˦/� 𳿺}ELܓ��w$�l|�ǩv�$0ݖL�m�7-v��gw���������5���rZ�������-�{1�3>��]� 0H��ە���έ��g�G�V�)�~�{L�%�O�����,P9hqf�2�(J��i�z���*�_1�>��o���E�/��L��DC��F�v������#��6Hr����$E�2���nœ6�Ɇ'�MO{�F�4���~*�{L�|��u���F�o8�Z/�N��̓x]��-x(퇣ٌ���'��T���{��?�?�A�0jg�     