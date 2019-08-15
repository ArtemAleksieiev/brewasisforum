--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.18
-- Dumped by pg_dump version 9.5.18

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: products; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.products (
    id integer NOT NULL,
    price numeric(15,6),
    name text
);


--
-- Name: sales; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.sales (
    id integer,
    sale_date date DEFAULT ('now'::text)::date NOT NULL,
    count integer
);


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.products (id, price, name) FROM stdin;
1	2.990000	Beer
2	1.990000	King Beer
\.


--
-- Data for Name: sales; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.sales (id, sale_date, count) FROM stdin;
\.


--
-- Name: products_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: sales_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sales
    ADD CONSTRAINT sales_id_fkey FOREIGN KEY (id) REFERENCES public.products(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: -
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

