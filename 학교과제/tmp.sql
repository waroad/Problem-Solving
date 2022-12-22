create table institute(
    institute_name    varchar2(30) not null primary key
);

create table academy(
    academy_name    varchar2(1000) not null,
    academy_foundation_date date  not null,
    ins_name    varchar(30)  not null,
    primary key (academy_name),
    foreign key (ins_name) references institute (institute_name)
);

create table journal(
    unique_journal_ID   number  not null,
    views   number,
    title  varchar2(500),
    open_to varchar2(50),
    publication_date    date    not null,
    cited_by    number,
    vol_num   number  not null,
    aca_name varchar2(150)   not null,
    primary key(unique_journal_ID),
    constraint aca_name_fk
    foreign key (aca_name) references academy (academy_name)
);

create table keyword(
    j_id number not null,
    keyword_text    varchar2(50)    not null,
    primary key (j_id, keyword_text),
    foreign key (j_id) references journal (unique_journal_id)
);


create table subscriber(
    subscriber_id   number  not null,
    starting_date   date    not null,
    validation_due  date    not null,
    subscriber_type varchar2(30) not null,
    name   varchar2(100) not null,
    primary key (subscriber_id)
);


create table rating(
    star    number,
    written_date    date    not null,
    sub_id  number  not null,
    j_id    number  not null,
    primary key(sub_id, j_id),
    foreign key (sub_id) references subscriber (subscriber_id),
    foreign key (j_id) references journal (unique_journal_ID)
);

create table citing(
    j_id number not null,
    citing_journal_id   varchar2(100)    not null,
    primary key (j_id, citing_journal_id),
    foreign key (j_id) references journal (unique_journal_ID)
);

create table academyworker(
    unique_worker_id    number  not null,
    F_name   varchar2(50) not null,
    L_name   varchar2(50) not null,
    department  varchar2(50) not null,
    aca_name  varchar2(1000)  not null,
    salary  number  not null,
    primary key (unique_worker_id),
    foreign key (aca_name) references academy (academy_name)
);


create table manages(
    ins_name  varchar2(30)  not null,
    sub_id  number  not null,
    primary key(ins_name, sub_id),
    foreign key (ins_name) references institute (institute_name),
    foreign key (sub_id) references subscriber (subscriber_id)
);

create table author(
    unique_author_ID number not null,
    F_name   varchar2(50) not null,
    L_name   varchar2(50) not null,
    primary key (unique_author_ID)
);

create table writes(
    a_id    number  not null,
    j_id    number  not null,
    primary key (a_id, j_id),
    foreign key (a_id) references author (unique_author_ID),
    foreign key (j_id) references journal (unique_journal_ID)
);

create table degree(
    a_id    number  not null,
    degree_text varchar(200),
    primary key (a_id, degree_text),
    foreign key (a_id) references author (unique_author_ID)
);


create table proposal(
    w_id    number  not null,
    a_id    number  not null,
    proposal_date   date    not null,
    accepted    varchar2(100)   not null,
    primary key(w_id, a_id, proposal_date),
    foreign key (w_id) references academyworker (unique_worker_id),
    foreign key (a_id) references author (unique_author_ID)
);

create table review(
    unique_review_id    number  not null,
    review_date     date    not null,
    review_text        varchar2(1000)    not null,
    j_id    number  not null,
    a_id    number  not null,
    primary key(unique_review_id),
    foreign key (a_id) references author (unique_author_ID),
    foreign key (j_id) references journal (unique_journal_ID)
);