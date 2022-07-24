--
-- PostgreSQL database dump
--

-- Dumped from database version 13.6
-- Dumped by pg_dump version 13.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: autor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.autor (
    id integer NOT NULL,
    cpf character varying(256) NOT NULL,
    nome character varying(256) NOT NULL,
    data_nascimento character varying(256) NOT NULL,
    endereco_id integer
);


ALTER TABLE public.autor OWNER TO postgres;

--
-- Name: autor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.autor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.autor_id_seq OWNER TO postgres;

--
-- Name: autor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.autor_id_seq OWNED BY public.autor.id;


--
-- Name: cidade; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cidade (
    id integer NOT NULL,
    sigla character varying(256) NOT NULL,
    nome character varying(256) NOT NULL
);


ALTER TABLE public.cidade OWNER TO postgres;

--
-- Name: cidade_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cidade_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cidade_id_seq OWNER TO postgres;

--
-- Name: cidade_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cidade_id_seq OWNED BY public.cidade.id;


--
-- Name: endereco; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.endereco (
    id integer NOT NULL,
    cep character varying(256) NOT NULL,
    logradouro character varying(256) NOT NULL,
    complemento character varying(256) NOT NULL,
    numero integer NOT NULL,
    cidade_id integer,
    estado_id integer,
    pais_id integer
);


ALTER TABLE public.endereco OWNER TO postgres;

--
-- Name: endereco_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.endereco_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.endereco_id_seq OWNER TO postgres;

--
-- Name: endereco_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.endereco_id_seq OWNED BY public.endereco.id;


--
-- Name: estado; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estado (
    id integer NOT NULL,
    sigla character varying(256) NOT NULL,
    nome character varying(256) NOT NULL
);


ALTER TABLE public.estado OWNER TO postgres;

--
-- Name: estado_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.estado_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.estado_id_seq OWNER TO postgres;

--
-- Name: estado_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.estado_id_seq OWNED BY public.estado.id;


--
-- Name: pais; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pais (
    id integer NOT NULL,
    sigla character varying(256) NOT NULL,
    nome character varying(256) NOT NULL
);


ALTER TABLE public.pais OWNER TO postgres;

--
-- Name: pais_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pais_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pais_id_seq OWNER TO postgres;

--
-- Name: pais_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pais_id_seq OWNED BY public.pais.id;


--
-- Name: autor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.autor ALTER COLUMN id SET DEFAULT nextval('public.autor_id_seq'::regclass);


--
-- Name: cidade id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cidade ALTER COLUMN id SET DEFAULT nextval('public.cidade_id_seq'::regclass);


--
-- Name: endereco id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco ALTER COLUMN id SET DEFAULT nextval('public.endereco_id_seq'::regclass);


--
-- Name: estado id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estado ALTER COLUMN id SET DEFAULT nextval('public.estado_id_seq'::regclass);


--
-- Name: pais id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pais ALTER COLUMN id SET DEFAULT nextval('public.pais_id_seq'::regclass);


--
-- Data for Name: autor; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.autor VALUES (1, '111.222.333-00', 'Jon Arbuckle', '28-07-1951', 3);
INSERT INTO public.autor VALUES (2, '222.333.444-11', 'Duda Dursleys', '23-06-1980', 4);
INSERT INTO public.autor VALUES (3, '333.444.555-33', 'Sirius Black', '03-11-1959', 5);
INSERT INTO public.autor VALUES (4, '444.555.666-44', 'Sherlock Holmes', '06-01-1854', 6);
INSERT INTO public.autor VALUES (5, '555.666.777-55', 'Clark Kent', '29-02-1938', 7);
INSERT INTO public.autor VALUES (6, '666.777.888-66', 'Doc Brown', '31-05-1920', 8);


--
-- Data for Name: cidade; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.cidade VALUES (1, 'Tenn', 'Tennessee');
INSERT INTO public.cidade VALUES (2, 'Lt. Whing.', 'Little Whinging');
INSERT INTO public.cidade VALUES (3, 'Ld', 'London');
INSERT INTO public.cidade VALUES (4, 'Mtp.', 'Metropolis');
INSERT INTO public.cidade VALUES (5, 'H. Val.', 'Hill Valley');


--
-- Data for Name: endereco; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.endereco VALUES (3, '21.222-000', 'Maple Street', 'null', 711, 1, 4, 1);
INSERT INTO public.endereco VALUES (4, '20.410-66', 'Privet Drive', 'null', 4, 2, 1, 2);
INSERT INTO public.endereco VALUES (5, '21381-666', 'Grimmauld Place', 'null', 12, 3, 5, 3);
INSERT INTO public.endereco VALUES (6, '11.321-000', 'Baker Street', 'B', 221, 3, 5, 3);
INSERT INTO public.endereco VALUES (7, '22.852-123', 'Clinton St.', 'Apt. 3B', 344, 4, 2, 1);
INSERT INTO public.endereco VALUES (8, '21478-123', 'Riverside Drive', 'Casa 07', 1640, 5, 3, 1);


--
-- Data for Name: estado; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.estado VALUES (1, 'Surr', 'Surrey');
INSERT INTO public.estado VALUES (2, 'NY', 'New York');
INSERT INTO public.estado VALUES (3, 'CA', 'California');
INSERT INTO public.estado VALUES (4, 'Tenn', 'Tennessee');
INSERT INTO public.estado VALUES (5, 'UK', 'United Kingdom');


--
-- Data for Name: pais; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.pais VALUES (1, 'USA', 'United States of America');
INSERT INTO public.pais VALUES (2, 'UK', 'United Kingdom');
INSERT INTO public.pais VALUES (3, 'ENG', 'England');


--
-- Name: autor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.autor_id_seq', 6, true);


--
-- Name: cidade_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cidade_id_seq', 5, true);


--
-- Name: endereco_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.endereco_id_seq', 8, true);


--
-- Name: estado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.estado_id_seq', 5, true);


--
-- Name: pais_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pais_id_seq', 3, true);


--
-- Name: autor autor_cpf_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.autor
    ADD CONSTRAINT autor_cpf_key UNIQUE (cpf);


--
-- Name: autor autor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.autor
    ADD CONSTRAINT autor_pkey PRIMARY KEY (id);


--
-- Name: cidade cidade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cidade
    ADD CONSTRAINT cidade_pkey PRIMARY KEY (id);


--
-- Name: endereco endereco_logradouro_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_logradouro_key UNIQUE (logradouro);


--
-- Name: endereco endereco_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_pkey PRIMARY KEY (id);


--
-- Name: estado estado_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estado
    ADD CONSTRAINT estado_pkey PRIMARY KEY (id);


--
-- Name: pais pais_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pais
    ADD CONSTRAINT pais_pkey PRIMARY KEY (id);


--
-- Name: autor autor_endereco_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.autor
    ADD CONSTRAINT autor_endereco_id_fkey FOREIGN KEY (endereco_id) REFERENCES public.endereco(id);


--
-- Name: endereco endereco_cidade_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_cidade_id_fkey FOREIGN KEY (cidade_id) REFERENCES public.cidade(id);


--
-- Name: endereco endereco_estado_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_estado_id_fkey FOREIGN KEY (estado_id) REFERENCES public.estado(id);


--
-- Name: endereco endereco_pais_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.endereco
    ADD CONSTRAINT endereco_pais_id_fkey FOREIGN KEY (pais_id) REFERENCES public.pais(id);


--
-- PostgreSQL database dump complete
--

